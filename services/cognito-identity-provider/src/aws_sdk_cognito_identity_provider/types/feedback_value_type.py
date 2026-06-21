"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#FeedbackValueType``."""

from typing import Literal, TypeAlias, cast

FeedbackValueType: TypeAlias = Literal[
    "Valid",
    "Invalid",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FeedbackValueType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FeedbackValueType:
    return cast(FeedbackValueType, data)
