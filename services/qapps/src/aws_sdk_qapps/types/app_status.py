"""Generated from Smithy shape ``com.amazonaws.qapps#AppStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qapps.errors import DeserializationError

AppStatus: TypeAlias = Literal[
    "PUBLISHED",
    "DRAFT",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PUBLISHED",
        "DRAFT",
        "DELETED",
    )
)


def serialize_json(value: AppStatus) -> str:
    return value


def deserialize_json(data: str) -> AppStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppStatus value: {data!r}")
    return cast(AppStatus, data)
