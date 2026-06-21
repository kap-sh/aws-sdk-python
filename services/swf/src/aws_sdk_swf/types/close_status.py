"""Generated from Smithy shape ``com.amazonaws.swf#CloseStatus``."""

from typing import Literal, TypeAlias, cast

CloseStatus: TypeAlias = Literal[
    "COMPLETED",
    "FAILED",
    "CANCELED",
    "TERMINATED",
    "CONTINUED_AS_NEW",
    "TIMED_OUT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloseStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CloseStatus:
    return cast(CloseStatus, data)
