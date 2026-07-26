"""Generated from Smithy shape ``com.amazonaws.bedrockagent#SharePointAuthType``."""

from typing import Literal, TypeAlias, cast

SharePointAuthType: TypeAlias = Literal[
    "OAUTH2_CLIENT_CREDENTIALS",
    "OAUTH2_SHAREPOINT_APP_ONLY_CLIENT_CREDENTIALS",
]


# --- restJson1 ser/de ---
def serialize_json(value: SharePointAuthType) -> str:
    return value


def deserialize_json(data: str) -> SharePointAuthType:
    return cast(SharePointAuthType, data)
