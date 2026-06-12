"""Generated from Smithy shape ``com.amazonaws.codebuild#SharedResourceSortByType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codebuild.errors import DeserializationError

SharedResourceSortByType: TypeAlias = Literal[
    "ARN",
    "MODIFIED_TIME",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ARN",
        "MODIFIED_TIME",
    )
)


def serialize_aws_json_1_1(value: SharedResourceSortByType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SharedResourceSortByType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SharedResourceSortByType value: {data!r}")
    return cast(SharedResourceSortByType, data)
