"""Generated from Smithy shape ``com.amazonaws.glue#TransformStatusType``."""

from typing import Literal, TypeAlias, cast

TransformStatusType: TypeAlias = Literal[
    "NOT_READY",
    "READY",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformStatusType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TransformStatusType:
    return cast(TransformStatusType, data)
