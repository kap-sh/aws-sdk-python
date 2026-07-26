"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#RegionSwitchPlanConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import capo_arc_region_switch.types.iam_role_arn
    import capo_arc_region_switch.types.plan_arn


class RegionSwitchPlanConfiguration(TypedDict, closed=True):
    cross_account_role: NotRequired[
        "capo_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross account role for the configuration.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the configuration.</p>"""
    arn: "capo_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the plan configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegionSwitchPlanConfiguration) -> dict:
    out: dict = {}
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RegionSwitchPlanConfiguration:
    out: RegionSwitchPlanConfiguration = {}  # type: ignore[typeddict-item]
    if "crossAccountRole" in data:
        out["cross_account_role"] = data["crossAccountRole"]
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("RegionSwitchPlanConfiguration.arn required")
    return out
