"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortTrialsBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SortTrialsBy: TypeAlias = Literal[
    "Name",
    "CreationTime",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
    )
)


def serialize_aws_json_1_1(value: SortTrialsBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortTrialsBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortTrialsBy value: {data!r}")
    return cast(SortTrialsBy, data)
