"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#PromotionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_personalize_runtime.types.promotion

PromotionList: TypeAlias = list["aws_sdk_personalize_runtime.types.promotion.Promotion"]


# --- restJson1 ser/de ---
def serialize_json(value: PromotionList) -> list:
    import aws_sdk_personalize_runtime.types.promotion

    out: list = []
    for item in value:
        out.append(aws_sdk_personalize_runtime.types.promotion.serialize_json(item))
    return out


def deserialize_json(data: list) -> PromotionList:
    import aws_sdk_personalize_runtime.types.promotion

    out: PromotionList = []
    for item in data:
        out.append(aws_sdk_personalize_runtime.types.promotion.deserialize_json(item))
    return out
