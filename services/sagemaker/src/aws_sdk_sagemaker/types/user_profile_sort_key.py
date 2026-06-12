"""Generated from Smithy shape ``com.amazonaws.sagemaker#UserProfileSortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

UserProfileSortKey: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: UserProfileSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserProfileSortKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UserProfileSortKey value: {data!r}")
    return cast(UserProfileSortKey, data)
