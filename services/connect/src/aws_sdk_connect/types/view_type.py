"""Generated from Smithy shape ``com.amazonaws.connect#ViewType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ViewType: TypeAlias = Literal[
    "CUSTOMER_MANAGED",
    "AWS_MANAGED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CUSTOMER_MANAGED",
        "AWS_MANAGED",
    )
)


def serialize_json(value: ViewType) -> str:
    return value


def deserialize_json(data: str) -> ViewType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ViewType value: {data!r}")
    return cast(ViewType, data)
