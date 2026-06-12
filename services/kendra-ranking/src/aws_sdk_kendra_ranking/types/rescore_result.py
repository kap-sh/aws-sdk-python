"""Generated from Smithy shape ``com.amazonaws.kendraranking#RescoreResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra_ranking.types.rescore_id
    import aws_sdk_kendra_ranking.types.rescore_result_item_list


class RescoreResult(TypedDict):
    rescore_id: NotRequired["aws_sdk_kendra_ranking.types.rescore_id.RescoreId"]
    """<p>The identifier associated with the scores that Amazon Kendra Intelligent Ranking gives to the results. Amazon Kendra Intelligent Ranking rescores or re-ranks the results for the search service.</p>"""
    result_items: NotRequired[
        "aws_sdk_kendra_ranking.types.rescore_result_item_list.RescoreResultItemList"
    ]
    """<p>A list of result items for documents with new relevancy scores. The results are in descending order.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RescoreResult) -> dict:
    out: dict = {}
    if "rescore_id" in value:
        out["RescoreId"] = value["rescore_id"]
    if "result_items" in value:
        import aws_sdk_kendra_ranking.types.rescore_result_item_list

        out["ResultItems"] = (
            aws_sdk_kendra_ranking.types.rescore_result_item_list.serialize_aws_json_1_0(
                value["result_items"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RescoreResult:
    out: RescoreResult = {}  # type: ignore[typeddict-item]
    if "RescoreId" in data:
        out["rescore_id"] = data["RescoreId"]
    if "ResultItems" in data:
        import aws_sdk_kendra_ranking.types.rescore_result_item_list

        out["result_items"] = (
            aws_sdk_kendra_ranking.types.rescore_result_item_list.deserialize_aws_json_1_0(
                data["ResultItems"]
            )
        )
    return out
