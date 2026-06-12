"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#ExpirationTimeResponse``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker_featurestore_runtime.errors import DeserializationError

ExpirationTimeResponse: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def serialize_json(value: ExpirationTimeResponse) -> str:
    return value


def deserialize_json(data: str) -> ExpirationTimeResponse:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExpirationTimeResponse value: {data!r}")
    return cast(ExpirationTimeResponse, data)
