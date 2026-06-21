"""Generated from Smithy shape ``com.amazonaws.mediaconvert#HlsOfflineEncrypted``."""

from typing import Literal, TypeAlias, cast

"""Enable this setting to insert the EXT-X-SESSION-KEY element into the master playlist. This allows for offline Apple HLS FairPlay content protection."""
HlsOfflineEncrypted: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: HlsOfflineEncrypted) -> str:
    return value


def deserialize_json(data: str) -> HlsOfflineEncrypted:
    return cast(HlsOfflineEncrypted, data)
