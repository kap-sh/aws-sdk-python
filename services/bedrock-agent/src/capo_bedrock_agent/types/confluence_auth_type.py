"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ConfluenceAuthType``."""

from typing import Literal, TypeAlias, cast

ConfluenceAuthType: TypeAlias = Literal[
    "BASIC",
    "OAUTH2_CLIENT_CREDENTIALS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfluenceAuthType) -> str:
    return value


def deserialize_json(data: str) -> ConfluenceAuthType:
    return cast(ConfluenceAuthType, data)
