"""Generated from Smithy shape ``com.amazonaws.auditmanager#SourceSetUpOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

SourceSetUpOption: TypeAlias = Literal[
    "System_Controls_Mapping",
    "Procedural_Controls_Mapping",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "System_Controls_Mapping",
        "Procedural_Controls_Mapping",
    )
)


def serialize_json(value: SourceSetUpOption) -> str:
    return value


def deserialize_json(data: str) -> SourceSetUpOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceSetUpOption value: {data!r}")
    return cast(SourceSetUpOption, data)
