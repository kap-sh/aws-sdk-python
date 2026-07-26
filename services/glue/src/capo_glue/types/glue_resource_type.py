"""Generated from Smithy shape ``com.amazonaws.glue#GlueResourceType``."""

from typing import Literal, TypeAlias, cast

GlueResourceType: TypeAlias = Literal[
    "JOB",
    "SESSION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlueResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GlueResourceType:
    return cast(GlueResourceType, data)
