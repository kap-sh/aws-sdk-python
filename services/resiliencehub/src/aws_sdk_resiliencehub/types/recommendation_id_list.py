"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RecommendationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.uuid

RecommendationIdList: TypeAlias = list["aws_sdk_resiliencehub.types.uuid.Uuid"]


# --- restJson1 ser/de ---
def serialize_json(value: RecommendationIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> RecommendationIdList:
    return list(data)
