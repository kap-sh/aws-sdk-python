"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EventFilterType``."""

from typing import Literal, TypeAlias, cast

EventFilterType: TypeAlias = Literal[
    "SIGN_IN",
    "PASSWORD_CHANGE",
    "SIGN_UP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EventFilterType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventFilterType:
    return cast(EventFilterType, data)
