"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelRegistrationMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelRegistrationMode: TypeAlias = Literal[
    "AutoModelRegistrationEnabled",
    "AutoModelRegistrationDisabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AutoModelRegistrationEnabled",
        "AutoModelRegistrationDisabled",
    )
)


def serialize_aws_json_1_1(value: ModelRegistrationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelRegistrationMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelRegistrationMode value: {data!r}")
    return cast(ModelRegistrationMode, data)
