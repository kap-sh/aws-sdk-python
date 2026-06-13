"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ListPlansResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.next_token
    import aws_sdk_arc_region_switch.types.plan_list


class ListPlansResponse(TypedDict):
    plans: NotRequired["aws_sdk_arc_region_switch.types.plan_list.PlanList"]
    """<p>The plans that were requested.</p>"""
    next_token: NotRequired["aws_sdk_arc_region_switch.types.next_token.NextToken"]
    """<p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListPlansResponse) -> dict:
    out: dict = {}
    if "plans" in value:
        import aws_sdk_arc_region_switch.types.plan_list

        out["plans"] = aws_sdk_arc_region_switch.types.plan_list.serialize_aws_json_1_0(
            value["plans"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListPlansResponse:
    out: ListPlansResponse = {}  # type: ignore[typeddict-item]
    if "plans" in data:
        import aws_sdk_arc_region_switch.types.plan_list

        out["plans"] = (
            aws_sdk_arc_region_switch.types.plan_list.deserialize_aws_json_1_0(
                data["plans"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
