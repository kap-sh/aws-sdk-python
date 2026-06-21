"""Generated from Smithy shape ``com.amazonaws.mpa#IdentitySourceStatusCode``."""

from typing import Literal, TypeAlias, cast

IdentitySourceStatusCode: TypeAlias = Literal[
    "ACCESS_DENIED",
    "DELETION_FAILED",
    "IDC_INSTANCE_NOT_FOUND",
    "IDC_INSTANCE_NOT_VALID",
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentitySourceStatusCode) -> str:
    return value


def deserialize_json(data: str) -> IdentitySourceStatusCode:
    return cast(IdentitySourceStatusCode, data)
