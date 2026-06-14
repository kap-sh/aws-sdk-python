"""Generated from Smithy shape ``com.amazonaws.datazone#FormTypeStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datazone.errors import DeserializationError

FormTypeStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: FormTypeStatus) -> str:
    return value


def deserialize_json(data: str) -> FormTypeStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FormTypeStatus value: {data!r}")
    return cast(FormTypeStatus, data)
