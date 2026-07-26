"""Generated from Smithy shape ``com.amazonaws.batch#ServiceEnvironmentType``."""

from typing import Literal, TypeAlias, cast

ServiceEnvironmentType: TypeAlias = Literal["SAGEMAKER_TRAINING",]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceEnvironmentType) -> str:
    return value


def deserialize_json(data: str) -> ServiceEnvironmentType:
    return cast(ServiceEnvironmentType, data)
