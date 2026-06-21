"""Generated from Smithy shape ``com.amazonaws.batch#ServiceJobType``."""

from typing import Literal, TypeAlias, cast

ServiceJobType: TypeAlias = Literal["SAGEMAKER_TRAINING",]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceJobType) -> str:
    return value


def deserialize_json(data: str) -> ServiceJobType:
    return cast(ServiceJobType, data)
