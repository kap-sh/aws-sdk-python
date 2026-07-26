"""Generated from Smithy shape ``com.amazonaws.pi#RecommendationIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pi.types.string

RecommendationIdList: TypeAlias = list["capo_pi.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationIdList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RecommendationIdList:
    return list(data)
