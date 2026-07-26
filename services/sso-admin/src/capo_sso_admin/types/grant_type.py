"""Generated from Smithy shape ``com.amazonaws.ssoadmin#GrantType``."""

from typing import Literal, TypeAlias, cast

GrantType: TypeAlias = Literal[
    "authorization_code",
    "refresh_token",
    "urn:ietf:params:oauth:grant-type:jwt-bearer",
    "urn:ietf:params:oauth:grant-type:token-exchange",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GrantType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GrantType:
    return cast(GrantType, data)
