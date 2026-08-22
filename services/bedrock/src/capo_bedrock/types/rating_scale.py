"""Generated from Smithy shape ``com.amazonaws.bedrock#RatingScale``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.rating_scale_item

RatingScale: TypeAlias = list["capo_bedrock.types.rating_scale_item.RatingScaleItem"]


# --- restJson1 ser/de ---
def serialize_json(value: RatingScale) -> list:
    import capo_bedrock.types.rating_scale_item

    out: list = []
    for item in value:
        out.append(capo_bedrock.types.rating_scale_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> RatingScale:
    import capo_bedrock.types.rating_scale_item

    out: RatingScale = []
    for item in data:
        if item is None:
            continue
        out.append(capo_bedrock.types.rating_scale_item.deserialize_json(item))
    return out
