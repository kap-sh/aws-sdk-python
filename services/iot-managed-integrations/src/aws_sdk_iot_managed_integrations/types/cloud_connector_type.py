"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CloudConnectorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot_managed_integrations.errors import DeserializationError

CloudConnectorType: TypeAlias = Literal[
    "LISTED",
    "UNLISTED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LISTED",
        "UNLISTED",
    )
)


def serialize_json(value: CloudConnectorType) -> str:
    return value


def deserialize_json(data: str) -> CloudConnectorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CloudConnectorType value: {data!r}")
    return cast(CloudConnectorType, data)
