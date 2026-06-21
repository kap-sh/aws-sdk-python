"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ClientAuthenticationMethodType``."""

from typing import Literal, TypeAlias, cast

ClientAuthenticationMethodType: TypeAlias = Literal[
    "CLIENT_SECRET_BASIC",
    "CLIENT_SECRET_POST",
    "AWS_IAM_ID_TOKEN_JWT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClientAuthenticationMethodType) -> str:
    return value


def deserialize_json(data: str) -> ClientAuthenticationMethodType:
    return cast(ClientAuthenticationMethodType, data)
