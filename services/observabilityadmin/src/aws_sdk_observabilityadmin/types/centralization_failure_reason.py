"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CentralizationFailureReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_observabilityadmin.errors import DeserializationError

CentralizationFailureReason: TypeAlias = Literal[
    "TRUSTED_ACCESS_NOT_ENABLED",
    "DESTINATION_ACCOUNT_NOT_IN_ORGANIZATION",
    "INTERNAL_SERVER_ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TRUSTED_ACCESS_NOT_ENABLED",
        "DESTINATION_ACCOUNT_NOT_IN_ORGANIZATION",
        "INTERNAL_SERVER_ERROR",
    )
)


def serialize_json(value: CentralizationFailureReason) -> str:
    return value


def deserialize_json(data: str) -> CentralizationFailureReason:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CentralizationFailureReason value: {data!r}"
        )
    return cast(CentralizationFailureReason, data)
