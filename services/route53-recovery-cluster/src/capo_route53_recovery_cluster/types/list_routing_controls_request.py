"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#ListRoutingControlsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53_recovery_cluster.types.arn
    import capo_route53_recovery_cluster.types.max_results
    import capo_route53_recovery_cluster.types.page_token


class ListRoutingControlsRequest(TypedDict, closed=True):
    control_panel_arn: NotRequired["capo_route53_recovery_cluster.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the control panel of the routing controls to list.</p>"""
    next_token: NotRequired["capo_route53_recovery_cluster.types.page_token.PageToken"]
    """<p>The token for the next set of results. You receive this token from a previous call.</p>"""
    max_results: NotRequired[
        "capo_route53_recovery_cluster.types.max_results.MaxResults"
    ]
    """<p>The number of routing controls objects that you want to return with this call. The default value is 500.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRoutingControlsRequest) -> dict:
    out: dict = {}
    if "control_panel_arn" in value:
        out["ControlPanelArn"] = value["control_panel_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRoutingControlsRequest:
    out: ListRoutingControlsRequest = {}  # type: ignore[typeddict-item]
    if "ControlPanelArn" in data:
        out["control_panel_arn"] = data["ControlPanelArn"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
