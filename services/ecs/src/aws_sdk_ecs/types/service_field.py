"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceField``."""

from typing import Literal, TypeAlias, cast

ServiceField: TypeAlias = Literal["TAGS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceField) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceField:
    return cast(ServiceField, data)
