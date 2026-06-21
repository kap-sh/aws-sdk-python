"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApiKeyCredentialLocation``."""

from typing import Literal, TypeAlias, cast

ApiKeyCredentialLocation: TypeAlias = Literal[
    "HEADER",
    "QUERY_PARAMETER",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApiKeyCredentialLocation) -> str:
    return value


def deserialize_json(data: str) -> ApiKeyCredentialLocation:
    return cast(ApiKeyCredentialLocation, data)
