"""Generated from Smithy shape ``com.amazonaws.lambda#ProvisionedConcurrencyStatusEnum``."""

from typing import Literal, TypeAlias, cast

ProvisionedConcurrencyStatusEnum: TypeAlias = Literal[
    "IN_PROGRESS",
    "READY",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionedConcurrencyStatusEnum) -> str:
    return value


def deserialize_json(data: str) -> ProvisionedConcurrencyStatusEnum:
    return cast(ProvisionedConcurrencyStatusEnum, data)
