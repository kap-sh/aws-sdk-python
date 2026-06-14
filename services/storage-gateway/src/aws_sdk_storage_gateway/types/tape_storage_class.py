"""Generated from Smithy shape ``com.amazonaws.storagegateway#TapeStorageClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_storage_gateway.errors import DeserializationError

TapeStorageClass: TypeAlias = Literal[
    "DEEP_ARCHIVE",
    "GLACIER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEEP_ARCHIVE",
        "GLACIER",
    )
)


def serialize_aws_json_1_1(value: TapeStorageClass) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TapeStorageClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TapeStorageClass value: {data!r}")
    return cast(TapeStorageClass, data)
