"""Generated from Smithy shape ``com.amazonaws.auditmanager#DeleteResources``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auditmanager.errors import DeserializationError

DeleteResources: TypeAlias = Literal[
    "ALL",
    "DEFAULT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALL",
        "DEFAULT",
    )
)


def serialize_json(value: DeleteResources) -> str:
    return value


def deserialize_json(data: str) -> DeleteResources:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeleteResources value: {data!r}")
    return cast(DeleteResources, data)
