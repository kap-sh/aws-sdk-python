"""Generated from Smithy shape ``com.amazonaws.quicksight#PredictQAResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.include_generated_answer
    import aws_sdk_quicksight.types.include_quick_sight_q_index
    import aws_sdk_quicksight.types.max_topics_to_consider
    import aws_sdk_quicksight.types.qa_query_text


class PredictQAResultsRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that the user wants to execute Predict QA results in.</p>"""
    query_text: "aws_sdk_quicksight.types.qa_query_text.QAQueryText"
    """<p>The query text to be used to predict QA results.</p>"""
    include_quick_sight_q_index: NotRequired[
        "aws_sdk_quicksight.types.include_quick_sight_q_index.IncludeQuickSightQIndex"
    ]
    """<p>Indicates whether Q indicies are included or excluded.</p>"""
    include_generated_answer: NotRequired[
        "aws_sdk_quicksight.types.include_generated_answer.IncludeGeneratedAnswer"
    ]
    """<p>Indicates whether generated answers are included or excluded.</p>"""
    max_topics_to_consider: NotRequired[
        "aws_sdk_quicksight.types.max_topics_to_consider.MaxTopicsToConsider"
    ]
    """<p>The number of maximum topics to be considered to predict QA results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PredictQAResultsRequest) -> dict:
    out: dict = {}
    out["QueryText"] = value["query_text"]
    if "include_quick_sight_q_index" in value:
        import aws_sdk_quicksight.types.include_quick_sight_q_index

        out["IncludeQuickSightQIndex"] = (
            aws_sdk_quicksight.types.include_quick_sight_q_index.serialize_json(
                value["include_quick_sight_q_index"]
            )
        )
    if "include_generated_answer" in value:
        import aws_sdk_quicksight.types.include_generated_answer

        out["IncludeGeneratedAnswer"] = (
            aws_sdk_quicksight.types.include_generated_answer.serialize_json(
                value["include_generated_answer"]
            )
        )
    if "max_topics_to_consider" in value:
        out["MaxTopicsToConsider"] = value["max_topics_to_consider"]
    return out


def deserialize_json(data: dict) -> PredictQAResultsRequest:
    out: PredictQAResultsRequest = {}  # type: ignore[typeddict-item]
    if "QueryText" in data:
        out["query_text"] = data["QueryText"]
    else:
        raise DeserializationError("PredictQAResultsRequest.query_text required")
    if "IncludeQuickSightQIndex" in data:
        import aws_sdk_quicksight.types.include_quick_sight_q_index

        out["include_quick_sight_q_index"] = (
            aws_sdk_quicksight.types.include_quick_sight_q_index.deserialize_json(
                data["IncludeQuickSightQIndex"]
            )
        )
    if "IncludeGeneratedAnswer" in data:
        import aws_sdk_quicksight.types.include_generated_answer

        out["include_generated_answer"] = (
            aws_sdk_quicksight.types.include_generated_answer.deserialize_json(
                data["IncludeGeneratedAnswer"]
            )
        )
    if "MaxTopicsToConsider" in data:
        out["max_topics_to_consider"] = data["MaxTopicsToConsider"]
    return out
