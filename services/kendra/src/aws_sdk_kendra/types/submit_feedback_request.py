"""Generated from Smithy shape ``com.amazonaws.kendra#SubmitFeedbackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.click_feedback_list
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.query_id
    import aws_sdk_kendra.types.relevance_feedback_list


class SubmitFeedbackRequest(TypedDict, closed=True):
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index that was queried.</p>"""
    query_id: "aws_sdk_kendra.types.query_id.QueryId"
    """<p>The identifier of the specific query for which you are submitting feedback. The query ID is returned in the response to the <code>Query</code> API.</p>"""
    click_feedback_items: NotRequired[
        "aws_sdk_kendra.types.click_feedback_list.ClickFeedbackList"
    ]
    """<p>Tells Amazon Kendra that a particular search result link was chosen by the user. </p>"""
    relevance_feedback_items: NotRequired[
        "aws_sdk_kendra.types.relevance_feedback_list.RelevanceFeedbackList"
    ]
    """<p>Provides Amazon Kendra with relevant or not relevant feedback for whether a particular item was relevant to the search.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubmitFeedbackRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["QueryId"] = value["query_id"]
    if "click_feedback_items" in value:
        import aws_sdk_kendra.types.click_feedback_list

        out["ClickFeedbackItems"] = (
            aws_sdk_kendra.types.click_feedback_list.serialize_aws_json_1_1(
                value["click_feedback_items"]
            )
        )
    if "relevance_feedback_items" in value:
        import aws_sdk_kendra.types.relevance_feedback_list

        out["RelevanceFeedbackItems"] = (
            aws_sdk_kendra.types.relevance_feedback_list.serialize_aws_json_1_1(
                value["relevance_feedback_items"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SubmitFeedbackRequest:
    out: SubmitFeedbackRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("SubmitFeedbackRequest.index_id required")
    if "QueryId" in data:
        out["query_id"] = data["QueryId"]
    else:
        raise DeserializationError("SubmitFeedbackRequest.query_id required")
    if "ClickFeedbackItems" in data:
        import aws_sdk_kendra.types.click_feedback_list

        out["click_feedback_items"] = (
            aws_sdk_kendra.types.click_feedback_list.deserialize_aws_json_1_1(
                data["ClickFeedbackItems"]
            )
        )
    if "RelevanceFeedbackItems" in data:
        import aws_sdk_kendra.types.relevance_feedback_list

        out["relevance_feedback_items"] = (
            aws_sdk_kendra.types.relevance_feedback_list.deserialize_aws_json_1_1(
                data["RelevanceFeedbackItems"]
            )
        )
    return out
