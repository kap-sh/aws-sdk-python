"""Generated from Smithy shape ``com.amazonaws.pcaconnectorscep#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
