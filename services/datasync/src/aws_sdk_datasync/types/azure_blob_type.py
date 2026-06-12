"""Generated from Smithy shape ``com.amazonaws.datasync#AzureBlobType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_datasync.errors import DeserializationError

AzureBlobType: TypeAlias = Literal["BLOCK",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("BLOCK",))


def serialize_aws_json_1_1(value: AzureBlobType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AzureBlobType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AzureBlobType value: {data!r}")
    return cast(AzureBlobType, data)
