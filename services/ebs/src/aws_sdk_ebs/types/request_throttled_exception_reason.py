"""Generated from Smithy shape ``com.amazonaws.ebs#RequestThrottledExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ebs.errors import DeserializationError

RequestThrottledExceptionReason: TypeAlias = Literal[
    "ACCOUNT_THROTTLED",
    "DEPENDENCY_REQUEST_THROTTLED",
    "RESOURCE_LEVEL_THROTTLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT_THROTTLED",
        "DEPENDENCY_REQUEST_THROTTLED",
        "RESOURCE_LEVEL_THROTTLE",
    )
)


def serialize_json(value: RequestThrottledExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> RequestThrottledExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RequestThrottledExceptionReason value: {data!r}"
        )
    return cast(RequestThrottledExceptionReason, data)
