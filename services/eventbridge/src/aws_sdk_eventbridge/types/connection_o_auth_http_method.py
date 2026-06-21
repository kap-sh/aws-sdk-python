"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectionOAuthHttpMethod``."""

from typing import Literal, TypeAlias, cast

ConnectionOAuthHttpMethod: TypeAlias = Literal[
    "GET",
    "POST",
    "PUT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionOAuthHttpMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConnectionOAuthHttpMethod:
    return cast(ConnectionOAuthHttpMethod, data)
