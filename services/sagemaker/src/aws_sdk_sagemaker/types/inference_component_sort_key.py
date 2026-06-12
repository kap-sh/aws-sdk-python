"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentSortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

InferenceComponentSortKey: TypeAlias = Literal[
    "Name",
    "CreationTime",
    "Status",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "CreationTime",
        "Status",
    )
)


def serialize_aws_json_1_1(value: InferenceComponentSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InferenceComponentSortKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InferenceComponentSortKey value: {data!r}")
    return cast(InferenceComponentSortKey, data)
