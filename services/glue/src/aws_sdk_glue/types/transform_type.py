"""Generated from Smithy shape ``com.amazonaws.glue#TransformType``."""

from typing import Literal, TypeAlias, cast

TransformType: TypeAlias = Literal["FIND_MATCHES",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TransformType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TransformType:
    return cast(TransformType, data)
