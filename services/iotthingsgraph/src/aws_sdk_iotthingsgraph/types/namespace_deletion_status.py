"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#NamespaceDeletionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotthingsgraph.errors import DeserializationError

NamespaceDeletionStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: NamespaceDeletionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NamespaceDeletionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NamespaceDeletionStatus value: {data!r}")
    return cast(NamespaceDeletionStatus, data)
