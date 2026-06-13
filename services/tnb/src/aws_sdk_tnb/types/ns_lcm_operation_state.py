"""Generated from Smithy shape ``com.amazonaws.tnb#NsLcmOperationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_tnb.errors import DeserializationError

NsLcmOperationState: TypeAlias = Literal[
    "PROCESSING",
    "COMPLETED",
    "FAILED",
    "CANCELLING",
    "CANCELLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROCESSING",
        "COMPLETED",
        "FAILED",
        "CANCELLING",
        "CANCELLED",
    )
)


def serialize_json(value: NsLcmOperationState) -> str:
    return value


def deserialize_json(data: str) -> NsLcmOperationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NsLcmOperationState value: {data!r}")
    return cast(NsLcmOperationState, data)
