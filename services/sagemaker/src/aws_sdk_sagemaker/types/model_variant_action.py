"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelVariantAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelVariantAction: TypeAlias = Literal[
    "Retain",
    "Remove",
    "Promote",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Retain",
        "Remove",
        "Promote",
    )
)


def serialize_aws_json_1_1(value: ModelVariantAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelVariantAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelVariantAction value: {data!r}")
    return cast(ModelVariantAction, data)
