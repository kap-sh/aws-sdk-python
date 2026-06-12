"""Generated from Smithy shape ``com.amazonaws.customerprofiles#StatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

StatusReason: TypeAlias = Literal[
    "VALIDATION_FAILURE",
    "INTERNAL_FAILURE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VALIDATION_FAILURE",
        "INTERNAL_FAILURE",
    )
)


def serialize_json(value: StatusReason) -> str:
    return value


def deserialize_json(data: str) -> StatusReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatusReason value: {data!r}")
    return cast(StatusReason, data)
