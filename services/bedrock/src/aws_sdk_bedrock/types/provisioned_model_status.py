"""Generated from Smithy shape ``com.amazonaws.bedrock#ProvisionedModelStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

ProvisionedModelStatus: TypeAlias = Literal[
    "Creating",
    "InService",
    "Updating",
    "Failed",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "InService",
        "Updating",
        "Failed",
    )
)


def serialize_json(value: ProvisionedModelStatus) -> str:
    return value


def deserialize_json(data: str) -> ProvisionedModelStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProvisionedModelStatus value: {data!r}")
    return cast(ProvisionedModelStatus, data)
