"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SharePointHostType``."""

from typing import Literal, TypeAlias, cast

SharePointHostType: TypeAlias = Literal["ONLINE",]


# --- restJson1 ser/de ---
def serialize_json(value: SharePointHostType) -> str:
    return value


def deserialize_json(data: str) -> SharePointHostType:
    return cast(SharePointHostType, data)
