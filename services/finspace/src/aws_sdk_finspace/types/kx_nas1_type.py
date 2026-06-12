"""Generated from Smithy shape ``com.amazonaws.finspace#KxNAS1Type``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace.errors import DeserializationError

KxNAS1Type: TypeAlias = Literal[
    "SSD_1000",
    "SSD_250",
    "HDD_12",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SSD_1000",
        "SSD_250",
        "HDD_12",
    )
)


def serialize_json(value: KxNAS1Type) -> str:
    return value


def deserialize_json(data: str) -> KxNAS1Type:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KxNAS1Type value: {data!r}")
    return cast(KxNAS1Type, data)
