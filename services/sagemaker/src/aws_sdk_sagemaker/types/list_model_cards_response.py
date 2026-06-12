"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListModelCardsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.model_card_summary_list
    import aws_sdk_sagemaker.types.next_token


class ListModelCardsResponse(TypedDict):
    model_card_summaries: NotRequired[
        "aws_sdk_sagemaker.types.model_card_summary_list.ModelCardSummaryList"
    ]
    """<p>The summaries of the listed model cards.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker returns this token. To retrieve the next set of model cards, use it in the subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListModelCardsResponse) -> dict:
    out: dict = {}
    if "model_card_summaries" in value:
        import aws_sdk_sagemaker.types.model_card_summary_list

        out["ModelCardSummaries"] = (
            aws_sdk_sagemaker.types.model_card_summary_list.serialize_aws_json_1_1(
                value["model_card_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListModelCardsResponse:
    out: ListModelCardsResponse = {}  # type: ignore[typeddict-item]
    if "ModelCardSummaries" in data:
        import aws_sdk_sagemaker.types.model_card_summary_list

        out["model_card_summaries"] = (
            aws_sdk_sagemaker.types.model_card_summary_list.deserialize_aws_json_1_1(
                data["ModelCardSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
