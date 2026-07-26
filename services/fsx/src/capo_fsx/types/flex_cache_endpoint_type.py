"""Generated from Smithy shape ``com.amazonaws.fsx#FlexCacheEndpointType``."""

from typing import Literal, TypeAlias, cast

FlexCacheEndpointType: TypeAlias = Literal[
    "NONE",
    "ORIGIN",
    "CACHE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FlexCacheEndpointType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FlexCacheEndpointType:
    return cast(FlexCacheEndpointType, data)
