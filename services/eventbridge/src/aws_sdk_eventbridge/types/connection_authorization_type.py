"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectionAuthorizationType``."""

from typing import Literal, TypeAlias, cast

ConnectionAuthorizationType: TypeAlias = Literal[
    "BASIC",
    "OAUTH_CLIENT_CREDENTIALS",
    "API_KEY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionAuthorizationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionAuthorizationType:
    return cast(ConnectionAuthorizationType, data)
