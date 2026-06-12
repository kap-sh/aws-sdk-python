"""Generated from Smithy shape ``com.amazonaws.sagemaker#ManagedStorageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ManagedStorageType: TypeAlias = Literal["Restricted",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Restricted",))


def serialize_aws_json_1_1(value: ManagedStorageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedStorageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ManagedStorageType value: {data!r}")
    return cast(ManagedStorageType, data)
