"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_scep.errors import DeserializationError

ValidationExceptionReason: TypeAlias = Literal[
    "CA_CERT_VALIDITY_TOO_SHORT",
    "INVALID_CA_USAGE_MODE",
    "INVALID_CONNECTOR_TYPE",
    "INVALID_STATE",
    "NO_CLIENT_TOKEN",
    "UNKNOWN_OPERATION",
    "OTHER",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CA_CERT_VALIDITY_TOO_SHORT",
        "INVALID_CA_USAGE_MODE",
        "INVALID_CONNECTOR_TYPE",
        "INVALID_STATE",
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
