"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#GetPlanInRegionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.plan_arn


class GetPlanInRegionRequest(TypedDict, closed=True):
    arn: "aws_sdk_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan in Region.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetPlanInRegionRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetPlanInRegionRequest:
    out: GetPlanInRegionRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetPlanInRegionRequest.arn required")
    return out
