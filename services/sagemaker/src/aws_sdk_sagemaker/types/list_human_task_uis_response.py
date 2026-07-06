"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListHumanTaskUisResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.human_task_ui_summaries
    import aws_sdk_sagemaker.types.next_token


class ListHumanTaskUisResponse(TypedDict, closed=True):
    human_task_ui_summaries: NotRequired[
        "aws_sdk_sagemaker.types.human_task_ui_summaries.HumanTaskUiSummaries"
    ]
    """<p>An array of objects describing the human task user interfaces.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>A token to resume pagination.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHumanTaskUisResponse) -> dict:
    out: dict = {}
    if "human_task_ui_summaries" in value:
        import aws_sdk_sagemaker.types.human_task_ui_summaries

        out["HumanTaskUiSummaries"] = (
            aws_sdk_sagemaker.types.human_task_ui_summaries.serialize_aws_json_1_1(
                value["human_task_ui_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHumanTaskUisResponse:
    out: ListHumanTaskUisResponse = {}  # type: ignore[typeddict-item]
    if "HumanTaskUiSummaries" in data:
        import aws_sdk_sagemaker.types.human_task_ui_summaries

        out["human_task_ui_summaries"] = (
            aws_sdk_sagemaker.types.human_task_ui_summaries.deserialize_aws_json_1_1(
                data["HumanTaskUiSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
