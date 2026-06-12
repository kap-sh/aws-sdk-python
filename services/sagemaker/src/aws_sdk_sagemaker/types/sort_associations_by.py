"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortAssociationsBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SortAssociationsBy: TypeAlias = Literal[
    "SourceArn",
    "DestinationArn",
    "SourceType",
    "DestinationType",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SourceArn",
        "DestinationArn",
        "SourceType",
        "DestinationType",
        "CreationTime",
    )
)


def serialize_aws_json_1_1(value: SortAssociationsBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortAssociationsBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortAssociationsBy value: {data!r}")
    return cast(SortAssociationsBy, data)
