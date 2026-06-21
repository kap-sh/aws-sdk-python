"""Generated from Smithy shape ``com.amazonaws.memorydb#ServiceUpdateType``."""

from typing import Literal, TypeAlias, cast

ServiceUpdateType: TypeAlias = Literal["security-update",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceUpdateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ServiceUpdateType:
    return cast(ServiceUpdateType, data)
