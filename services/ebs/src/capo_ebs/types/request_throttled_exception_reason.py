"""Generated from Smithy shape ``com.amazonaws.ebs#RequestThrottledExceptionReason``."""

from typing import Literal, TypeAlias, cast

RequestThrottledExceptionReason: TypeAlias = Literal[
    "ACCOUNT_THROTTLED",
    "DEPENDENCY_REQUEST_THROTTLED",
    "RESOURCE_LEVEL_THROTTLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: RequestThrottledExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> RequestThrottledExceptionReason:
    return cast(RequestThrottledExceptionReason, data)
