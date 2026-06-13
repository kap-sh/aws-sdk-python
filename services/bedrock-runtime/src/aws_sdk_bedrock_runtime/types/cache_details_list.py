"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#CacheDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.cache_detail

CacheDetailsList: TypeAlias = list[
    "aws_sdk_bedrock_runtime.types.cache_detail.CacheDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: CacheDetailsList) -> list:
    import aws_sdk_bedrock_runtime.types.cache_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_runtime.types.cache_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> CacheDetailsList:
    import aws_sdk_bedrock_runtime.types.cache_detail

    out: CacheDetailsList = []
    for item in data:
        out.append(aws_sdk_bedrock_runtime.types.cache_detail.deserialize_json(item))
    return out
