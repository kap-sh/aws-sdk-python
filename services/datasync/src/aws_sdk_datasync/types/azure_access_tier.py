"""Generated from Smithy shape ``com.amazonaws.datasync#AzureAccessTier``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

AzureAccessTier: TypeAlias = Literal[
    "HOT",
    "COOL",
    "ARCHIVE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HOT",
        "COOL",
        "ARCHIVE",
    )
)


def serialize_aws_json_1_1(value: AzureAccessTier) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AzureAccessTier:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AzureAccessTier value: {data!r}")
    return cast(AzureAccessTier, data)
