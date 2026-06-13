"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_ad.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "FIELD_VALIDATION_FAILED",
    "INVALID_CA_SUBJECT",
    "INVALID_PERMISSION",
    "INVALID_STATE",
    "MISMATCHED_CONNECTOR",
    "MISMATCHED_VPC",
    "NO_CLIENT_TOKEN",
    "UNKNOWN_OPERATION",
    "OTHER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FIELD_VALIDATION_FAILED",
        "INVALID_CA_SUBJECT",
        "INVALID_PERMISSION",
        "INVALID_STATE",
        "MISMATCHED_CONNECTOR",
        "MISMATCHED_VPC",
        "NO_CLIENT_TOKEN",
        "UNKNOWN_OPERATION",
        "OTHER",
    )
)


def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ValidationExceptionReason value: {data!r}")
    return cast(ValidationExceptionReason, data)
