"""Generated from Smithy shape ``com.amazonaws.sagemaker#SpaceSortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SpaceSortKey: TypeAlias = Literal[
    "CreationTime",
    "LastModifiedTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CreationTime",
        "LastModifiedTime",
    )
)


def serialize_aws_json_1_1(value: SpaceSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SpaceSortKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SpaceSortKey value: {data!r}")
    return cast(SpaceSortKey, data)
