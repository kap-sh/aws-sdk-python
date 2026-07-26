"""Generated from Smithy shape ``com.amazonaws.kendraranking#RescoreResultItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kendra_ranking.types.rescore_result_item

RescoreResultItemList: TypeAlias = list[
    "capo_kendra_ranking.types.rescore_result_item.RescoreResultItem"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RescoreResultItemList) -> list:
    import capo_kendra_ranking.types.rescore_result_item

    out: list = []
    for item in value:
        out.append(
            capo_kendra_ranking.types.rescore_result_item.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RescoreResultItemList:
    import capo_kendra_ranking.types.rescore_result_item

    out: RescoreResultItemList = []
    for item in data:
        out.append(
            capo_kendra_ranking.types.rescore_result_item.deserialize_aws_json_1_0(item)
        )
    return out
