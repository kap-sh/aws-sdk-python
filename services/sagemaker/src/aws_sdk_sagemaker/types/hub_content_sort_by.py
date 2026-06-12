"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubContentSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

HubContentSortBy: TypeAlias = Literal[
    "HubContentName",
    "CreationTime",
    "HubContentStatus",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HubContentName",
        "CreationTime",
        "HubContentStatus",
    )
)


def serialize_aws_json_1_1(value: HubContentSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HubContentSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HubContentSortBy value: {data!r}")
    return cast(HubContentSortBy, data)
