"""Generated from Smithy shape ``com.amazonaws.inspector2#AssociationResultStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_inspector2.errors import DeserializationError

AssociationResultStatusCode: TypeAlias = Literal[
    "INTERNAL_ERROR",
    "ACCESS_DENIED",
    "SCAN_CONFIGURATION_NOT_FOUND",
    "INVALID_INPUT",
    "RESOURCE_NOT_FOUND",
    "QUOTA_EXCEEDED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INTERNAL_ERROR",
        "ACCESS_DENIED",
        "SCAN_CONFIGURATION_NOT_FOUND",
        "INVALID_INPUT",
        "RESOURCE_NOT_FOUND",
        "QUOTA_EXCEEDED",
    )
)


def serialize_json(value: AssociationResultStatusCode) -> str:
    return value


def deserialize_json(data: str) -> AssociationResultStatusCode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AssociationResultStatusCode value: {data!r}"
        )
    return cast(AssociationResultStatusCode, data)
