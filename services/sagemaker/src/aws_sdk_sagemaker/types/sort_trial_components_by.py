"""Generated from Smithy shape ``com.amazonaws.sagemaker#SortTrialComponentsBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SortTrialComponentsBy: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: SortTrialComponentsBy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SortTrialComponentsBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SortTrialComponentsBy value: {data!r}")
    return cast(SortTrialComponentsBy, data)
