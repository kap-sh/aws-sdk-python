"""Generated from Smithy shape ``com.amazonaws.lightsail#StatusType``."""

from typing import Literal, TypeAlias, cast

StatusType: TypeAlias = Literal[
    "Active",
    "Inactive",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StatusType:
    return cast(StatusType, data)
