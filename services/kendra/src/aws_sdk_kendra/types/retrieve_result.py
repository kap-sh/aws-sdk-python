"""Generated from Smithy shape ``com.amazonaws.kendra#RetrieveResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.query_id
    import aws_sdk_kendra.types.retrieve_result_item_list


class RetrieveResult(TypedDict, closed=True):
    query_id: NotRequired["aws_sdk_kendra.types.query_id.QueryId"]
    r"""<p>The identifier of query used for the search. You also use <code>QueryId</code> to identify the search when using the <a href=\"https://docs.aws.amazon.com/kendra/latest/APIReference/API_SubmitFeedback.html\">Submitfeedback</a> API.</p>"""
    result_items: NotRequired[
        "aws_sdk_kendra.types.retrieve_result_item_list.RetrieveResultItemList"
    ]
    """<p>The results of the retrieved relevant passages for the search.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RetrieveResult) -> dict:
    out: dict = {}
    if "query_id" in value:
        out["QueryId"] = value["query_id"]
    if "result_items" in value:
        import aws_sdk_kendra.types.retrieve_result_item_list

        out["ResultItems"] = (
            aws_sdk_kendra.types.retrieve_result_item_list.serialize_aws_json_1_1(
                value["result_items"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RetrieveResult:
    out: RetrieveResult = {}  # type: ignore[typeddict-item]
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    if "ResultItems" in data:
        import aws_sdk_kendra.types.retrieve_result_item_list

        out["result_items"] = (
            aws_sdk_kendra.types.retrieve_result_item_list.deserialize_aws_json_1_1(
                data["ResultItems"]
            )
        )
    return out
