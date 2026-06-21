"""Generated from Smithy shape ``com.amazonaws.batch#ServiceResourceIdName``."""

from typing import Literal, TypeAlias, cast

ServiceResourceIdName: TypeAlias = Literal["TrainingJobArn",]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceResourceIdName) -> str:
    return value


def deserialize_json(data: str) -> ServiceResourceIdName:
    return cast(ServiceResourceIdName, data)
