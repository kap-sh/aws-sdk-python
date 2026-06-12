"""Generated from Smithy shape ``com.amazonaws.appconfig#UpdateDeploymentStrategyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.deployment_strategy_id
    import aws_sdk_appconfig.types.description
    import aws_sdk_appconfig.types.growth_factor
    import aws_sdk_appconfig.types.growth_type
    import aws_sdk_appconfig.types.minutes_between0_and24_hours


class UpdateDeploymentStrategyRequest(TypedDict):
    deployment_strategy_id: (
        "aws_sdk_appconfig.types.deployment_strategy_id.DeploymentStrategyId"
    )
    """<p>The deployment strategy ID.</p>"""
    description: NotRequired["aws_sdk_appconfig.types.description.Description"]
    """<p>A description of the deployment strategy.</p>"""
    deployment_duration_in_minutes: NotRequired[
        "aws_sdk_appconfig.types.minutes_between0_and24_hours.MinutesBetween0And24Hours"
    ]
    """<p>Total amount of time for a deployment to last.</p>"""
    final_bake_time_in_minutes: NotRequired[
        "aws_sdk_appconfig.types.minutes_between0_and24_hours.MinutesBetween0And24Hours"
    ]
    """<p>The amount of time that AppConfig monitors for alarms before considering the deployment to be complete and no longer eligible for automatic rollback.</p>"""
    growth_factor: NotRequired["aws_sdk_appconfig.types.growth_factor.GrowthFactor"]
    """<p>The percentage of targets to receive a deployed configuration during each interval.</p>"""
    growth_type: NotRequired["aws_sdk_appconfig.types.growth_type.GrowthType"]
    """<p>The algorithm used to define how percentage grows over time. AppConfig supports the following growth types:</p> <p> <b>Linear</b>: For this type, AppConfig processes the deployment by increments of the growth factor evenly distributed over the deployment time. For example, a linear deployment that uses a growth factor of 20 initially makes the configuration available to 20 percent of the targets. After 1/5th of the deployment time has passed, the system updates the percentage to 40 percent. This continues until 100% of the targets are set to receive the deployed configuration.</p> <p> <b>Exponential</b>: For this type, AppConfig processes the deployment exponentially using the following formula: <code>G*(2^N)</code>. In this formula, <code>G</code> is the growth factor specified by the user and <code>N</code> is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows:</p> <p> <code>2*(2^0)</code> </p> <p> <code>2*(2^1)</code> </p> <p> <code>2*(2^2)</code> </p> <p>Expressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDeploymentStrategyRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "deployment_duration_in_minutes" in value:
        out["DeploymentDurationInMinutes"] = value["deployment_duration_in_minutes"]
    if "final_bake_time_in_minutes" in value:
        out["FinalBakeTimeInMinutes"] = value["final_bake_time_in_minutes"]
    if "growth_factor" in value:
        out["GrowthFactor"] = value["growth_factor"]
    if "growth_type" in value:
        import aws_sdk_appconfig.types.growth_type

        out["GrowthType"] = aws_sdk_appconfig.types.growth_type.serialize_json(
            value["growth_type"]
        )
    return out


def deserialize_json(data: dict) -> UpdateDeploymentStrategyRequest:
    out: UpdateDeploymentStrategyRequest = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DeploymentDurationInMinutes" in data:
        out["deployment_duration_in_minutes"] = data["DeploymentDurationInMinutes"]
    if "FinalBakeTimeInMinutes" in data:
        out["final_bake_time_in_minutes"] = data["FinalBakeTimeInMinutes"]
    if "GrowthFactor" in data:
        out["growth_factor"] = data["GrowthFactor"]
    if "GrowthType" in data:
        import aws_sdk_appconfig.types.growth_type

        out["growth_type"] = aws_sdk_appconfig.types.growth_type.deserialize_json(
            data["GrowthType"]
        )
    return out
