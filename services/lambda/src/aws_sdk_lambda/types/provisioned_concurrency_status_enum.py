"""Generated from Smithy shape ``com.amazonaws.lambda#ProvisionedConcurrencyStatusEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

ProvisionedConcurrencyStatusEnum: TypeAlias = Literal[
    "IN_PROGRESS",
    "READY",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "READY",
        "FAILED",
    )
)


def serialize_json(value: ProvisionedConcurrencyStatusEnum) -> str:
    return value


def deserialize_json(data: str) -> ProvisionedConcurrencyStatusEnum:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProvisionedConcurrencyStatusEnum value: {data!r}"
        )
    return cast(ProvisionedConcurrencyStatusEnum, data)
