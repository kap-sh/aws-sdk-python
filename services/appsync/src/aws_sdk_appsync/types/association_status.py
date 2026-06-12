"""Generated from Smithy shape ``com.amazonaws.appsync#AssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appsync.errors import DeserializationError

AssociationStatus: TypeAlias = Literal[
    "PROCESSING",
    "FAILED",
    "SUCCESS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PROCESSING",
        "FAILED",
        "SUCCESS",
    )
)


def serialize_json(value: AssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> AssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssociationStatus value: {data!r}")
    return cast(AssociationStatus, data)
