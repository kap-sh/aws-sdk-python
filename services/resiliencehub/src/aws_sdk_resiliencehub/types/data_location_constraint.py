"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DataLocationConstraint``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

DataLocationConstraint: TypeAlias = Literal[
    "AnyLocation",
    "SameContinent",
    "SameCountry",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AnyLocation",
        "SameContinent",
        "SameCountry",
    )
)


def serialize_json(value: DataLocationConstraint) -> str:
    return value


def deserialize_json(data: str) -> DataLocationConstraint:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataLocationConstraint value: {data!r}")
    return cast(DataLocationConstraint, data)
