"""Generated from Smithy shape ``com.amazonaws.bedrock#RatingScale``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.rating_scale_item

RatingScale: TypeAlias = list["aws_sdk_bedrock.types.rating_scale_item.RatingScaleItem"]


# --- restJson1 ser/de ---
def serialize_json(value: RatingScale) -> list:
    import aws_sdk_bedrock.types.rating_scale_item

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock.types.rating_scale_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> RatingScale:
    import aws_sdk_bedrock.types.rating_scale_item

    out: RatingScale = []
    for item in data:
        out.append(aws_sdk_bedrock.types.rating_scale_item.deserialize_json(item))
    return out
