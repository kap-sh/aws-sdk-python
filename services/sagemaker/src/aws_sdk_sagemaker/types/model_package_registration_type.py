"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelPackageRegistrationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelPackageRegistrationType: TypeAlias = Literal[
    "Logged",
    "Registered",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Logged",
        "Registered",
    )
)


def serialize_aws_json_1_1(value: ModelPackageRegistrationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelPackageRegistrationType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ModelPackageRegistrationType value: {data!r}"
        )
    return cast(ModelPackageRegistrationType, data)
