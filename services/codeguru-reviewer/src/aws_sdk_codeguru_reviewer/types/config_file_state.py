"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#ConfigFileState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeguru_reviewer.errors import DeserializationError

ConfigFileState: TypeAlias = Literal[
    "Present",
    "Absent",
    "PresentWithErrors",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Present",
        "Absent",
        "PresentWithErrors",
    )
)


def serialize_json(value: ConfigFileState) -> str:
    return value


def deserialize_json(data: str) -> ConfigFileState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigFileState value: {data!r}")
    return cast(ConfigFileState, data)
