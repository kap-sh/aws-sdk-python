"""Generated from Smithy shape ``com.amazonaws.swf#RequestCancelActivityTaskFailedCause``."""

from typing import Literal, TypeAlias, cast

RequestCancelActivityTaskFailedCause: TypeAlias = Literal[
    "ACTIVITY_ID_UNKNOWN",
    "OPERATION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RequestCancelActivityTaskFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RequestCancelActivityTaskFailedCause:
    return cast(RequestCancelActivityTaskFailedCause, data)
