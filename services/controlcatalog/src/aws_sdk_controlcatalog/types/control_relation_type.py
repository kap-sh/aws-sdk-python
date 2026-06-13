"""Generated from Smithy shape ``com.amazonaws.controlcatalog#ControlRelationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_controlcatalog.errors import DeserializationError

ControlRelationType: TypeAlias = Literal[
    "COMPLEMENTARY",
    "ALTERNATIVE",
    "MUTUALLY_EXCLUSIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COMPLEMENTARY",
        "ALTERNATIVE",
        "MUTUALLY_EXCLUSIVE",
    )
)


def serialize_json(value: ControlRelationType) -> str:
    return value


def deserialize_json(data: str) -> ControlRelationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ControlRelationType value: {data!r}")
    return cast(ControlRelationType, data)
