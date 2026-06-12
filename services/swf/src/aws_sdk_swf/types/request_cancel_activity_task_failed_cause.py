"""Generated from Smithy shape ``com.amazonaws.swf#RequestCancelActivityTaskFailedCause``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_swf.errors import DeserializationError

RequestCancelActivityTaskFailedCause: TypeAlias = Literal[
    "ACTIVITY_ID_UNKNOWN",
    "OPERATION_NOT_PERMITTED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVITY_ID_UNKNOWN",
        "OPERATION_NOT_PERMITTED",
    )
)


def serialize_aws_json_1_0(value: RequestCancelActivityTaskFailedCause) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RequestCancelActivityTaskFailedCause:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RequestCancelActivityTaskFailedCause value: {data!r}"
        )
    return cast(RequestCancelActivityTaskFailedCause, data)
