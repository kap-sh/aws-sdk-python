"""Generated from Smithy shape ``com.amazonaws.workdocs#ShareStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

ShareStatusType: TypeAlias = Literal[
    "SUCCESS",
    "FAILURE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCESS",
        "FAILURE",
    )
)


def serialize_json(value: ShareStatusType) -> str:
    return value


def deserialize_json(data: str) -> ShareStatusType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ShareStatusType value: {data!r}")
    return cast(ShareStatusType, data)
