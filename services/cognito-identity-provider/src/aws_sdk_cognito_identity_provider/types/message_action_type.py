"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#MessageActionType``."""

from typing import Literal, TypeAlias, cast

MessageActionType: TypeAlias = Literal[
    "RESEND",
    "SUPPRESS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MessageActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MessageActionType:
    return cast(MessageActionType, data)
