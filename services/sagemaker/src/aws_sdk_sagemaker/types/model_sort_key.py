"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelSortKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelSortKey: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ModelSortKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelSortKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelSortKey value: {data!r}")
    return cast(ModelSortKey, data)
