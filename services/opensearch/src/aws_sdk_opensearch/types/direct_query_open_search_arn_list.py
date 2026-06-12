"""Generated from Smithy shape ``com.amazonaws.opensearch#DirectQueryOpenSearchARNList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.arn

DirectQueryOpenSearchARNList: TypeAlias = list["aws_sdk_opensearch.types.arn.ARN"]


# --- restJson1 ser/de ---
def serialize_json(value: DirectQueryOpenSearchARNList) -> list:
    return list(value)


def deserialize_json(data: list) -> DirectQueryOpenSearchARNList:
    return list(data)
