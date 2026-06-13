"""Generated from Smithy shape ``com.amazonaws.quicksight#FlowPublishState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

FlowPublishState: TypeAlias = Literal[
    "PUBLISHED",
    "DRAFT",
    "PENDING_APPROVAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLISHED",
        "DRAFT",
        "PENDING_APPROVAL",
    )
)


def serialize_json(value: FlowPublishState) -> str:
    return value


def deserialize_json(data: str) -> FlowPublishState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FlowPublishState value: {data!r}")
    return cast(FlowPublishState, data)
