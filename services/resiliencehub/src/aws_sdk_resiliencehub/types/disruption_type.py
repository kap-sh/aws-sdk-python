"""Generated from Smithy shape ``com.amazonaws.resiliencehub#DisruptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

DisruptionType: TypeAlias = Literal[
    "Software",
    "Hardware",
    "AZ",
    "Region",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Software",
        "Hardware",
        "AZ",
        "Region",
    )
)


def serialize_json(value: DisruptionType) -> str:
    return value


def deserialize_json(data: str) -> DisruptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DisruptionType value: {data!r}")
    return cast(DisruptionType, data)
