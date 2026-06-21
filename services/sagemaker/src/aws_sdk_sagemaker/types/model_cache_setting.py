"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelCacheSetting``."""

from typing import Literal, TypeAlias, cast

ModelCacheSetting: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelCacheSetting) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ModelCacheSetting:
    return cast(ModelCacheSetting, data)
