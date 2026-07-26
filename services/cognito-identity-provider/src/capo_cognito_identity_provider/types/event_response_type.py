"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EventResponseType``."""

from typing import Literal, TypeAlias, cast

EventResponseType: TypeAlias = Literal[
    "Pass",
    "Fail",
    "InProgress",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventResponseType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventResponseType:
    return cast(EventResponseType, data)
