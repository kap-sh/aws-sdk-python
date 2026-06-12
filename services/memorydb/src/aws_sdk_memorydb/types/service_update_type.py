"""Generated from Smithy shape ``com.amazonaws.memorydb#ServiceUpdateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_memorydb.errors import DeserializationError

ServiceUpdateType: TypeAlias = Literal["security-update",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("security-update",))


def serialize_aws_json_1_1(value: ServiceUpdateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceUpdateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceUpdateType value: {data!r}")
    return cast(ServiceUpdateType, data)
