"""Generated from Smithy shape ``com.amazonaws.ecs#EBSResourceType``."""

from typing import Literal, TypeAlias, cast

EBSResourceType: TypeAlias = Literal["volume",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EBSResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EBSResourceType:
    return cast(EBSResourceType, data)
