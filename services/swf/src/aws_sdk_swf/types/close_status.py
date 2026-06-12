"""Generated from Smithy shape ``com.amazonaws.swf#CloseStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

CloseStatus: TypeAlias = Literal[
    "COMPLETED",
    "FAILED",
    "CANCELED",
    "TERMINATED",
    "CONTINUED_AS_NEW",
    "TIMED_OUT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLETED",
        "FAILED",
        "CANCELED",
        "TERMINATED",
        "CONTINUED_AS_NEW",
        "TIMED_OUT",
    )
)


def serialize_aws_json_1_0(value: CloseStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CloseStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CloseStatus value: {data!r}")
    return cast(CloseStatus, data)
