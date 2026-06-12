"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_resiliencehub.errors import DeserializationError

AppStatusType: TypeAlias = Literal[
    "Active",
    "Deleting",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Deleting",
    )
)


def serialize_json(value: AppStatusType) -> str:
    return value


def deserialize_json(data: str) -> AppStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppStatusType value: {data!r}")
    return cast(AppStatusType, data)
