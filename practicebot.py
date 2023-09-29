
intents = discord.Intents.default()
intents.members = True
intents.voice_states = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Dictionary to store member join times for practice room voice chat
practice_room_join_times = {}
# Dictionary to store member total practice time
practice_time_dict = {}
# Dictionary to store member reminders
reminders = {}

# ID of the channel where practice times will be announced
practice_time_channel_id = 
  # Replace with your channel ID

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_member_join(member):
    # Check if the member joined the practice room channel
    # Record their join time and user ID into practice_room_join_times
    pass

@bot.event
async def on_voice_state_update(member, before, after):
    practice_room_channel_id = 
      # Replace with your practice room channel ID

    if before.channel and before.channel.id == practice_room_channel_id:
        # Member left the practice room voice channel
        if member.id in practice_room_join_times:
            join_time = practice_room_join_times[member.id]
            leave_time = datetime.datetime.now()
            time_spent = leave_time - join_time

            if member.id in practice_time_dict:
                practice_time_dict[member.id] += time_spent
            else:
                practice_time_dict[member.id] = time_spent

            del practice_room_join_times[member.id]

            # Announce practice time in the specified channel
            channel = bot.get_channel(practice_time_channel_id)
            await channel.send(f"{member.mention} practiced for: {time_spent}")

@bot.command()
async def leaderboard(ctx, period):
    # Implement leaderboard functionality (daily, weekly, monthly)
    pass

@bot.command()
async def set_reminder(ctx, time):
    # Allow users to set reminders
    member = ctx.author
    reminders[member.id] = time
    await ctx.send(f"Reminder set for {member.mention}: {time}")

@bot.command()
async def toggle_reminder(ctx):
    # Implement toggle reminder functionality
    member = ctx.author
    if member.id in reminders:
        del reminders[member.id]
        await ctx.send(f"Reminder turned off for {member.mention}")
    else:
        await ctx.send(f"No reminder set for {member.mention}")

@bot.command()
async def practice_time(ctx):
    member = ctx.author
    if member.id in practice_time_dict:
        total_time = practice_time_dict[member.id]
        await ctx.send(f"Total practice time: {total_time}")
    else:
        await ctx.send("You haven't spent any time in the practice room yet.")

bot.run('')

