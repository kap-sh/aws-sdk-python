"""Generated from Smithy shape ``com.amazonaws.sagemaker#SearchSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SearchSortOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Ascending",
        "Descending",
    )
)


def serialize_aws_json_1_1(value: SearchSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SearchSortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SearchSortOrder value: {data!r}")
    return cast(SearchSortOrder, data)
