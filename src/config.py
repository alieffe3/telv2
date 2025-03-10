from typing import Dict, List

class ChannelConfig:
    def __init__(self, url: str, enabled: bool = True, retry_count: int = 0):
        self.url = url
        self.enabled = enabled
        self.retry_count = retry_count
        self.success_rate = 100.0

class ProxyConfig:
    def __init__(self):
        self.TELEGRAM_CHANNELS = [
            ChannelConfig("https://t.me/s/ShadowProxy66"),
            ChannelConfig("https://t.me/s/DirectVPN"),
            ChannelConfig("https://t.me/s/v2ray_configs_pool"),
            ChannelConfig("https://t.me/s/Parsashonam"),
            ChannelConfig("https://t.me/s/v2nodes"),
            ChannelConfig("https://t.me/s/xs_filternet"),
            ChannelConfig("https://t.me/s/PrivateVPNs"),
            ChannelConfig("https://t.me/s/Hope_Net"), 
            ChannelConfig("https://t.me/s/oneclickvpnkeys"),
            ChannelConfig("https://t.me/s/ELiV2RAY"),
            ChannelConfig("https://t.me/s/V2rayNGX"),
            ChannelConfig("https://t.me/s/DailyV2RY"),
            ChannelConfig("https://t.me/s/xs_filternet"),
            ChannelConfig("https://t.me/s/mobilesignal"),
            ChannelConfig("https://t.me/s/ISVvpn"),
            ChannelConfig("https://t.me/s/proxy_kafee"),
            ChannelConfig("https://t.me/s/v2Line"),
            ChannelConfig("https://t.me/s/vpnowl"),
            ChannelConfig("https://raw.githubusercontent.com/roosterkid/openproxylist/main/V2RAY_BASE64.txt"),
            ChannelConfig("https://Rayan-Config.github.io/ALL"),
            ChannelConfig("https://raw.githubusercontent.com/Mosifree/-FREE2CONFIG/refs/heads/main/T,H"),
            ChannelConfig("https://raw.githubusercontent.com/valid7996/Gozargah/refs/heads/main/Gozargah_Sub"),
            ChannelConfig("https://raw.githubusercontent.com/Vahidqaz/BESTIIVPNBOT/refs/heads/main/BESTIIVPNBOT.txt"),
            ChannelConfig("https://t.me/s/melov2ray")
        ]

        self.PROTOCOL_CONFIG_LIMITS = {
            "min": 10,
            "max": 35
        }

        self.SUPPORTED_PROTOCOLS: Dict[str, Dict] = {
            #"wireguard://": {"min_configs": self.PROTOCOL_CONFIG_LIMITS["min"], "max_configs": self.PROTOCOL_CONFIG_LIMITS["max"]},
            "hysteria2://": {"min_configs": self.PROTOCOL_CONFIG_LIMITS["min"], "max_configs": self.PROTOCOL_CONFIG_LIMITS["max"]},
            "vless://": {"min_configs": self.PROTOCOL_CONFIG_LIMITS["min"], "max_configs": self.PROTOCOL_CONFIG_LIMITS["max"]},
            "vmess://": {"min_configs": self.PROTOCOL_CONFIG_LIMITS["min"], "max_configs": self.PROTOCOL_CONFIG_LIMITS["max"]},
            "ss://": {"min_configs": self.PROTOCOL_CONFIG_LIMITS["min"], "max_configs": self.PROTOCOL_CONFIG_LIMITS["max"]},
            "trojan://": {"min_configs": self.PROTOCOL_CONFIG_LIMITS["min"], "max_configs": self.PROTOCOL_CONFIG_LIMITS["max"]}
        }

        self.MIN_CONFIGS_PER_CHANNEL = 10
        self.MAX_CONFIGS_PER_CHANNEL = 40
        self.MAX_CONFIG_AGE_DAYS = 14
        self.CHANNEL_RETRY_LIMIT = 10
        self.CHANNEL_ERROR_THRESHOLD = 0.5

        self.MIN_PROTOCOL_RATIO = 0.15

        self.OUTPUT_FILE = 'configs/proxy_configs.txt'
        self.STATS_FILE = 'configs/channel_stats.json'

        self.MAX_RETRIES = 3
        self.RETRY_DELAY = 5
        self.REQUEST_TIMEOUT = 30

        self.HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

    def is_protocol_enabled(self, protocol: str) -> bool:
        return protocol in self.SUPPORTED_PROTOCOLS

    def get_enabled_channels(self) -> List[ChannelConfig]:
        return [channel for channel in self.TELEGRAM_CHANNELS if channel.enabled]

    def update_channel_stats(self, channel: ChannelConfig, success: bool):
        channel.retry_count = 0 if success else channel.retry_count + 1
        
        weight = 0.5
        new_rate = 100.0 if success else 0.0
        channel.success_rate = (weight * new_rate) + ((1 - weight) * channel.success_rate)
        
        if channel.success_rate < self.CHANNEL_ERROR_THRESHOLD * 100:
            channel.enabled = False
