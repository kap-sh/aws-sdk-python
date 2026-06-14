"""Generated from Smithy shape ``com.amazonaws.storagegateway#PoolStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_storage_gateway.errors import DeserializationError

PoolStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETED",
    )
)


def serialize_aws_json_1_1(value: PoolStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PoolStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PoolStatus value: {data!r}")
    return cast(PoolStatus, data)
