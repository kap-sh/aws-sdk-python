"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#StatusType``."""

from typing import Literal, TypeAlias, cast

StatusType: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StatusType:
    return cast(StatusType, data)
