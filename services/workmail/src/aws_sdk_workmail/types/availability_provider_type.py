"""Generated from Smithy shape ``com.amazonaws.workmail#AvailabilityProviderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workmail.errors import DeserializationError

AvailabilityProviderType: TypeAlias = Literal[
    "EWS",
    "LAMBDA",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EWS",
        "LAMBDA",
    )
)


def serialize_aws_json_1_1(value: AvailabilityProviderType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AvailabilityProviderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AvailabilityProviderType value: {data!r}")
    return cast(AvailabilityProviderType, data)
