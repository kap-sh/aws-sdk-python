"""Generated from Smithy shape ``com.amazonaws.sagemaker#AutoMLSortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AutoMLSortOrder: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: AutoMLSortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutoMLSortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoMLSortOrder value: {data!r}")
    return cast(AutoMLSortOrder, data)
