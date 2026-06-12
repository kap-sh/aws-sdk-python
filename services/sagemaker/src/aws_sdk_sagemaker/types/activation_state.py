"""Generated from Smithy shape ``com.amazonaws.sagemaker#ActivationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ActivationState: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def serialize_aws_json_1_1(value: ActivationState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActivationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActivationState value: {data!r}")
    return cast(ActivationState, data)
