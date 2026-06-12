"""Generated from Smithy shape ``com.amazonaws.sagemaker#SkipModelValidation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

SkipModelValidation: TypeAlias = Literal[
    "All",
    "None",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "All",
        "None",
    )
)


def serialize_aws_json_1_1(value: SkipModelValidation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SkipModelValidation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SkipModelValidation value: {data!r}")
    return cast(SkipModelValidation, data)
