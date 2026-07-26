"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#DeletePlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_region_switch.types.plan_arn


class DeletePlanRequest(TypedDict, closed=True):
    arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeletePlanRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeletePlanRequest:
    out: DeletePlanRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeletePlanRequest.arn required")
    return out
