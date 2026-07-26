"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#ValidationExceptionReason``."""

from typing import Literal, TypeAlias, cast

ValidationExceptionReason: TypeAlias = Literal[
    "INVALID_PAGINATION_TOKEN",
    "MALFORMED_REQUEST_PARAMETERS",
    "PAGINATION_LIMIT_EXCEEDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionReason) -> str:
    return value


def deserialize_json(data: str) -> ValidationExceptionReason:
    return cast(ValidationExceptionReason, data)
