"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EventSourceName``."""

from typing import Literal, TypeAlias, cast

EventSourceName: TypeAlias = Literal[
    "userNotification",
    "userAuthEvents",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventSourceName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventSourceName:
    return cast(EventSourceName, data)
