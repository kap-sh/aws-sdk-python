"""Generated from Smithy shape ``com.amazonaws.securityhub#AssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

AssociationStatus: TypeAlias = Literal[
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


def serialize_json(value: AssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> AssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssociationStatus value: {data!r}")
    return cast(AssociationStatus, data)
