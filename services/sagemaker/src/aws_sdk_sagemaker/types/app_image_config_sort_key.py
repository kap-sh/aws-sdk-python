"""Generated from Smithy shape ``com.amazonaws.sagemaker#AppImageConfigSortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AppImageConfigSortKey: TypeAlias = Literal[
    "CreationTime",
    "LastModifiedTime",
    "Name",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CreationTime",
        "LastModifiedTime",
        "Name",
    )
)


def serialize_aws_json_1_1(value: AppImageConfigSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AppImageConfigSortKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AppImageConfigSortKey value: {data!r}")
    return cast(AppImageConfigSortKey, data)
