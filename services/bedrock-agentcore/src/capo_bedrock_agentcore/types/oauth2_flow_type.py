"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Oauth2FlowType``."""

from typing import Literal, TypeAlias, cast

Oauth2FlowType: TypeAlias = Literal[
    "USER_FEDERATION",
    "M2M",
    "ON_BEHALF_OF_TOKEN_EXCHANGE",
]


# --- restJson1 ser/de ---
def serialize_json(value: Oauth2FlowType) -> str:
    return value


def deserialize_json(data: str) -> Oauth2FlowType:
    return cast(Oauth2FlowType, data)
