"""Generated from Smithy shape ``com.amazonaws.sagemaker#HubSortBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

HubSortBy: TypeAlias = Literal[
    "HubName",
    "CreationTime",
    "HubStatus",
    "AccountIdOwner",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HubName",
        "CreationTime",
        "HubStatus",
        "AccountIdOwner",
    )
)


def serialize_aws_json_1_1(value: HubSortBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HubSortBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HubSortBy value: {data!r}")
    return cast(HubSortBy, data)
