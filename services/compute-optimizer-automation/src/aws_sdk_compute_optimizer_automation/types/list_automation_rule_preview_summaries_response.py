"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAutomationRulePreviewSummariesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.next_token
    import aws_sdk_compute_optimizer_automation.types.preview_result_summaries


class ListAutomationRulePreviewSummariesResponse(TypedDict, closed=True):
    preview_result_summaries: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.preview_result_summaries.PreviewResultSummaries"
    ]
    """<p>The list of automation rule preview summaries that match the specified criteria.</p>"""
    next_token: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p>A token used for pagination. If present, indicates there are more results available and can be used in subsequent requests.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutomationRulePreviewSummariesResponse) -> dict:
    out: dict = {}
    if "preview_result_summaries" in value:
        import aws_sdk_compute_optimizer_automation.types.preview_result_summaries

        out["previewResultSummaries"] = (
            aws_sdk_compute_optimizer_automation.types.preview_result_summaries.serialize_aws_json_1_0(
                value["preview_result_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutomationRulePreviewSummariesResponse:
    out: ListAutomationRulePreviewSummariesResponse = {}  # type: ignore[typeddict-item]
    if "previewResultSummaries" in data:
        import aws_sdk_compute_optimizer_automation.types.preview_result_summaries

        out["preview_result_summaries"] = (
            aws_sdk_compute_optimizer_automation.types.preview_result_summaries.deserialize_aws_json_1_0(
                data["previewResultSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
