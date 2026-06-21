"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityProviderField``."""

from typing import Literal, TypeAlias, cast

CapacityProviderField: TypeAlias = Literal["TAGS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityProviderField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityProviderField:
    return cast(CapacityProviderField, data)
