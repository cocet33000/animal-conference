require 'slack-api'
# 先ほどのTokenを下に入力
TOKEN = 'xoxp-440767144820-440232906752-441137893685-19c47b9af0aa9b209243eb0f87a90ada'

Slack.configure do |conf|
  conf.token = TOKEN
end

client = Slack::RealTime::Client.new

client.on :hello do
  puts 'connected!'
  client.message channel: 'your_channel_id', text: 'connected!'
end
