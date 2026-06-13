"""Generated from Smithy shape ``com.amazonaws.taxsettings#HeritageStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_taxsettings.errors import DeserializationError

HeritageStatus: TypeAlias = Literal[
    "OptIn",
    "OptOut",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OptIn",
        "OptOut",
    )
)


def serialize_json(value: HeritageStatus) -> str:
    return value


def deserialize_json(data: str) -> HeritageStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HeritageStatus value: {data!r}")
    return cast(HeritageStatus, data)
