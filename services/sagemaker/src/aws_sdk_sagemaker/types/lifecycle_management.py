"""Generated from Smithy shape ``com.amazonaws.sagemaker#LifecycleManagement``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

LifecycleManagement: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: LifecycleManagement) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LifecycleManagement:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LifecycleManagement value: {data!r}")
    return cast(LifecycleManagement, data)
