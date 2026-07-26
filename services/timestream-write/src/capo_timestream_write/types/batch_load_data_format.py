"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#BatchLoadDataFormat``."""

from typing import Literal, TypeAlias, cast

BatchLoadDataFormat: TypeAlias = Literal["CSV",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchLoadDataFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BatchLoadDataFormat:
    return cast(BatchLoadDataFormat, data)
