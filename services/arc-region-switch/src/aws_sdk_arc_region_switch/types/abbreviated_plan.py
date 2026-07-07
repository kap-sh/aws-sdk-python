"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#AbbreviatedPlan``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_arc_region_switch.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_arc_region_switch.types.account_id
    import aws_sdk_arc_region_switch.types.execution_id
    import aws_sdk_arc_region_switch.types.plan_arn
    import aws_sdk_arc_region_switch.types.plan_name
    import aws_sdk_arc_region_switch.types.recovery_approach
    import aws_sdk_arc_region_switch.types.region
    import aws_sdk_arc_region_switch.types.region_list


class AbbreviatedPlan(TypedDict, closed=True):
    arn: "aws_sdk_arc_region_switch.types.plan_arn.PlanArn"
    """<p>The Amazon Resource Name (ARN) of the Region switch plan.</p>"""
    owner: "aws_sdk_arc_region_switch.types.account_id.AccountId"
    """<p>The owner of a Region switch plan.</p>"""
    name: "aws_sdk_arc_region_switch.types.plan_name.PlanName"
    """<p>The name of a Region switch plan.</p>"""
    regions: "aws_sdk_arc_region_switch.types.region_list.RegionList"
    """<p>The Amazon Web Services Region specified for a Region switch plan.</p>"""
    recovery_approach: (
        "aws_sdk_arc_region_switch.types.recovery_approach.RecoveryApproach"
    )
    """<p>The recovery approach for a Region switch plan, which can be active/active (activeActive) or active/passive (activePassive).</p>"""
    primary_region: NotRequired["aws_sdk_arc_region_switch.types.region.Region"]
    """<p>The primary Region for a plan.</p>"""
    version: NotRequired["str"]
    """<p>The version for the plan.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the plan execution was last updated.</p>"""
    description: NotRequired["str"]
    """<p>The description of a Region switch plan.</p>"""
    execution_role: NotRequired["str"]
    """<p>The execution role is a way to categorize a Region switch plan. </p>"""
    active_plan_execution: NotRequired[
        "aws_sdk_arc_region_switch.types.execution_id.ExecutionId"
    ]
    """<p>Specifies if this is the active plan execution at this time.</p>"""
    recovery_time_objective_minutes: NotRequired["int"]
    """<p>The recovery time objective that you've specified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AbbreviatedPlan) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["owner"] = value["owner"]
    out["name"] = value["name"]
    import aws_sdk_arc_region_switch.types.region_list

    out["regions"] = aws_sdk_arc_region_switch.types.region_list.serialize_aws_json_1_0(
        value["regions"]
    )
    import aws_sdk_arc_region_switch.types.recovery_approach

    out["recoveryApproach"] = (
        aws_sdk_arc_region_switch.types.recovery_approach.serialize_aws_json_1_0(
            value["recovery_approach"]
        )
    )
    if "primary_region" in value:
        out["primaryRegion"] = value["primary_region"]
    if "version" in value:
        out["version"] = value["version"]
    if "updated_at" in value:
        import aws_sdk_arc_region_switch.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_arc_region_switch.types._prelude.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "execution_role" in value:
        out["executionRole"] = value["execution_role"]
    if "active_plan_execution" in value:
        out["activePlanExecution"] = value["active_plan_execution"]
    if "recovery_time_objective_minutes" in value:
        out["recoveryTimeObjectiveMinutes"] = value["recovery_time_objective_minutes"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AbbreviatedPlan:
    out: AbbreviatedPlan = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AbbreviatedPlan.arn required")
    if "owner" in data:
        out["owner"] = data["owner"]
    else:
        raise DeserializationError("AbbreviatedPlan.owner required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("AbbreviatedPlan.name required")
    if "regions" in data:
        import aws_sdk_arc_region_switch.types.region_list

        out["regions"] = (
            aws_sdk_arc_region_switch.types.region_list.deserialize_aws_json_1_0(
                data["regions"]
            )
        )
    else:
        raise DeserializationError("AbbreviatedPlan.regions required")
    if "recoveryApproach" in data:
        import aws_sdk_arc_region_switch.types.recovery_approach

        out["recovery_approach"] = (
            aws_sdk_arc_region_switch.types.recovery_approach.deserialize_aws_json_1_0(
                data["recoveryApproach"]
            )
        )
    else:
        raise DeserializationError("AbbreviatedPlan.recovery_approach required")
    if "primaryRegion" in data:
        out["primary_region"] = data["primaryRegion"]
    if "version" in data:
        out["version"] = data["version"]
    if "updatedAt" in data:
        import aws_sdk_arc_region_switch.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_arc_region_switch.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "executionRole" in data:
        out["execution_role"] = data["executionRole"]
    if "activePlanExecution" in data:
        out["active_plan_execution"] = data["activePlanExecution"]
    if "recoveryTimeObjectiveMinutes" in data:
        out["recovery_time_objective_minutes"] = data["recoveryTimeObjectiveMinutes"]
    return out
