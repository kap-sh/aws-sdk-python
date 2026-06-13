"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#UpdatePlanResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_arc_region_switch.types.plan


class UpdatePlanResponse(TypedDict):
    plan: NotRequired["aws_sdk_arc_region_switch.types.plan.Plan"]
    """<p>The details of the updated Region switch plan.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdatePlanResponse) -> dict:
    out: dict = {}
    if "plan" in value:
        import aws_sdk_arc_region_switch.types.plan

        out["plan"] = aws_sdk_arc_region_switch.types.plan.serialize_aws_json_1_0(
            value["plan"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdatePlanResponse:
    out: UpdatePlanResponse = {}  # type: ignore[typeddict-item]
    if "plan" in data:
        import aws_sdk_arc_region_switch.types.plan

        out["plan"] = aws_sdk_arc_region_switch.types.plan.deserialize_aws_json_1_0(
            data["plan"]
        )
    return out
