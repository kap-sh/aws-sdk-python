"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListRecommendedActionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.next_token
    import aws_sdk_compute_optimizer_automation.types.recommended_actions


class ListRecommendedActionsResponse(TypedDict):
    recommended_actions: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.recommended_actions.RecommendedActions"
    ]
    """<p> The list of recommended actions that match the specified criteria. </p>"""
    next_token: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p>A token used for pagination. If present, indicates there are more results available and can be used in subsequent requests.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRecommendedActionsResponse) -> dict:
    out: dict = {}
    if "recommended_actions" in value:
        import aws_sdk_compute_optimizer_automation.types.recommended_actions

        out["recommendedActions"] = (
            aws_sdk_compute_optimizer_automation.types.recommended_actions.serialize_aws_json_1_0(
                value["recommended_actions"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRecommendedActionsResponse:
    out: ListRecommendedActionsResponse = {}  # type: ignore[typeddict-item]
    if "recommendedActions" in data:
        import aws_sdk_compute_optimizer_automation.types.recommended_actions

        out["recommended_actions"] = (
            aws_sdk_compute_optimizer_automation.types.recommended_actions.deserialize_aws_json_1_0(
                data["recommendedActions"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
