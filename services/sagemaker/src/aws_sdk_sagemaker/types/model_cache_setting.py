"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCacheSetting``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

ModelCacheSetting: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ModelCacheSetting) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCacheSetting:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ModelCacheSetting value: {data!r}")
    return cast(ModelCacheSetting, data)
