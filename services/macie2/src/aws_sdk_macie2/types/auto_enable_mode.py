"""Generated from Smithy shape ``com.amazonaws.macie2#AutoEnableMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_macie2.errors import DeserializationError

"""<p>Specifies whether to automatically enable automated sensitive data discovery for accounts that are part of an organization in Amazon Macie. Valid values are:</p>"""
AutoEnableMode: TypeAlias = Literal[
    "ALL",
    "NEW",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "NEW",
        "NONE",
    )
)


def serialize_json(value: AutoEnableMode) -> str:
    return value


def deserialize_json(data: str) -> AutoEnableMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoEnableMode value: {data!r}")
    return cast(AutoEnableMode, data)
