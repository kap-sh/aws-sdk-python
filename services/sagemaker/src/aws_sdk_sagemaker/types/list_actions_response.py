"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListActionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.action_summaries
    import aws_sdk_sagemaker.types.next_token


class ListActionsResponse(TypedDict, closed=True):
    action_summaries: NotRequired[
        "aws_sdk_sagemaker.types.action_summaries.ActionSummaries"
    ]
    """<p>A list of actions and their properties.</p>"""
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>A token for getting the next set of actions, if there are any.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListActionsResponse) -> dict:
    out: dict = {}
    if "action_summaries" in value:
        import aws_sdk_sagemaker.types.action_summaries

        out["ActionSummaries"] = (
            aws_sdk_sagemaker.types.action_summaries.serialize_aws_json_1_1(
                value["action_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListActionsResponse:
    out: ListActionsResponse = {}  # type: ignore[typeddict-item]
    if "ActionSummaries" in data:
        import aws_sdk_sagemaker.types.action_summaries

        out["action_summaries"] = (
            aws_sdk_sagemaker.types.action_summaries.deserialize_aws_json_1_1(
                data["ActionSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
