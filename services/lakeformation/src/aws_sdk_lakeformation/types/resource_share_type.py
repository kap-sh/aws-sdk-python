"""Generated from Smithy shape ``com.amazonaws.lakeformation#ResourceShareType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lakeformation.errors import DeserializationError

ResourceShareType: TypeAlias = Literal[
    "FOREIGN",
    "ALL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FOREIGN",
        "ALL",
    )
)


def serialize_json(value: ResourceShareType) -> str:
    return value


def deserialize_json(data: str) -> ResourceShareType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceShareType value: {data!r}")
    return cast(ResourceShareType, data)
