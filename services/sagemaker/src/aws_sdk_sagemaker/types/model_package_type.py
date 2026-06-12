"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelPackageType: TypeAlias = Literal[
    "Versioned",
    "Unversioned",
    "Both",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Versioned",
        "Unversioned",
        "Both",
    )
)


def serialize_aws_json_1_1(value: ModelPackageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelPackageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelPackageType value: {data!r}")
    return cast(ModelPackageType, data)
