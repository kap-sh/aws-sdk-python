"""Generated from Smithy shape ``com.amazonaws.memorydb#ServiceUpdateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_memorydb.errors import DeserializationError

ServiceUpdateStatus: TypeAlias = Literal[
    "available",
    "in-progress",
    "complete",
    "scheduled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "available",
        "in-progress",
        "complete",
        "scheduled",
    )
)


def serialize_aws_json_1_1(value: ServiceUpdateStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceUpdateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServiceUpdateStatus value: {data!r}")
    return cast(ServiceUpdateStatus, data)
