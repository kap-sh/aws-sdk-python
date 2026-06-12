"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortQuotaBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SortQuotaBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
    "ClusterArn",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
        "Status",
        "ClusterArn",
    )
)


def serialize_aws_json_1_1(value: SortQuotaBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortQuotaBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortQuotaBy value: {data!r}")
    return cast(SortQuotaBy, data)
