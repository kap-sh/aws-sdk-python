"""Generated from Smithy shape ``com.amazonaws.ivs#StreamKeyArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ivs.types.stream_key_arn

StreamKeyArnList: TypeAlias = list["aws_sdk_ivs.types.stream_key_arn.StreamKeyArn"]


# --- restJson1 ser/de ---
def serialize_json(value: StreamKeyArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> StreamKeyArnList:
    return list(data)
