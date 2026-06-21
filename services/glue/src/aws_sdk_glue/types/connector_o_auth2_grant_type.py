"""Generated from Smithy shape ``com.amazonaws.glue#ConnectorOAuth2GrantType``."""

from typing import Literal, TypeAlias, cast

ConnectorOAuth2GrantType: TypeAlias = Literal[
    "CLIENT_CREDENTIALS",
    "JWT_BEARER",
    "AUTHORIZATION_CODE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectorOAuth2GrantType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectorOAuth2GrantType:
    return cast(ConnectorOAuth2GrantType, data)
