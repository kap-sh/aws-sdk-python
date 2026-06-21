"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CentralizationFailureReason``."""

from typing import Literal, TypeAlias, cast

CentralizationFailureReason: TypeAlias = Literal[
    "TRUSTED_ACCESS_NOT_ENABLED",
    "DESTINATION_ACCOUNT_NOT_IN_ORGANIZATION",
    "INTERNAL_SERVER_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: CentralizationFailureReason) -> str:
    return value


def deserialize_json(data: str) -> CentralizationFailureReason:
    return cast(CentralizationFailureReason, data)
