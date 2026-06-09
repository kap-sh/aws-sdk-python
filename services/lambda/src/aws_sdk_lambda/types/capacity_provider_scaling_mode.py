"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProviderScalingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lambda.errors import DeserializationError

CapacityProviderScalingMode: TypeAlias = Literal[
    "Auto",
    "Manual",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Auto",
        "Manual",
    )
)


def serialize_json(value: CapacityProviderScalingMode) -> str:
    return value


def deserialize_json(data: str) -> CapacityProviderScalingMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CapacityProviderScalingMode value: {data!r}"
        )
    return cast(CapacityProviderScalingMode, data)
