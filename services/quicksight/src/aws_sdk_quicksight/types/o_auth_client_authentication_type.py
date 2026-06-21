"""Generated from Smithy shape ``com.amazonaws.quicksight#OAuthClientAuthenticationType``."""

from typing import Literal, TypeAlias, cast

OAuthClientAuthenticationType: TypeAlias = Literal["TOKEN",]


# --- restJson1 ser/de ---
def serialize_json(value: OAuthClientAuthenticationType) -> str:
    return value


def deserialize_json(data: str) -> OAuthClientAuthenticationType:
    return cast(OAuthClientAuthenticationType, data)
