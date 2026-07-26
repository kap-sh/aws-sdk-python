"""Generated from Smithy shape ``com.amazonaws.healthlake#PreloadDataType``."""

from typing import Literal, TypeAlias, cast

PreloadDataType: TypeAlias = Literal["SYNTHEA",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PreloadDataType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PreloadDataType:
    return cast(PreloadDataType, data)
