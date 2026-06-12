"""Generated from Smithy shape ``com.amazonaws.appconfig#DeploymentStrategy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.description
    import aws_sdk_appconfig.types.growth_type
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.minutes_between0_and24_hours
    import aws_sdk_appconfig.types.name
    import aws_sdk_appconfig.types.percentage
    import aws_sdk_appconfig.types.replicate_to


class DeploymentStrategy(TypedDict):
    id: NotRequired["aws_sdk_appconfig.types.id.Id"]
    """<p>The deployment strategy ID.</p>"""
    name: NotRequired["aws_sdk_appconfig.types.name.Name"]
    """<p>The name of the deployment strategy.</p>"""
    description: NotRequired["aws_sdk_appconfig.types.description.Description"]
    """<p>The description of the deployment strategy.</p>"""
    deployment_duration_in_minutes: (
        "aws_sdk_appconfig.types.minutes_between0_and24_hours.MinutesBetween0And24Hours"
    )
    """<p>Total amount of time the deployment lasted.</p>"""
    growth_type: NotRequired["aws_sdk_appconfig.types.growth_type.GrowthType"]
    """<p>The algorithm used to define how percentage grew over time.</p>"""
    growth_factor: NotRequired["aws_sdk_appconfig.types.percentage.Percentage"]
    """<p>The percentage of targets that received a deployed configuration during each interval.</p>"""
    final_bake_time_in_minutes: (
        "aws_sdk_appconfig.types.minutes_between0_and24_hours.MinutesBetween0And24Hours"
    )
    """<p>The amount of time that AppConfig monitored for alarms before considering the deployment to be complete and no longer eligible for automatic rollback.</p>"""
    replicate_to: NotRequired["aws_sdk_appconfig.types.replicate_to.ReplicateTo"]
    """<p>Save the deployment strategy to a Systems Manager (SSM) document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeploymentStrategy) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["DeploymentDurationInMinutes"] = value.get("deployment_duration_in_minutes", 0)
    if "growth_type" in value:
        import aws_sdk_appconfig.types.growth_type

        out["GrowthType"] = aws_sdk_appconfig.types.growth_type.serialize_json(
            value["growth_type"]
        )
    if "growth_factor" in value:
        out["GrowthFactor"] = value["growth_factor"]
    out["FinalBakeTimeInMinutes"] = value.get("final_bake_time_in_minutes", 0)
    if "replicate_to" in value:
        import aws_sdk_appconfig.types.replicate_to

        out["ReplicateTo"] = aws_sdk_appconfig.types.replicate_to.serialize_json(
            value["replicate_to"]
        )
    return out


def deserialize_json(data: dict) -> DeploymentStrategy:
    out: DeploymentStrategy = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "DeploymentDurationInMinutes" in data:
        out["deployment_duration_in_minutes"] = data["DeploymentDurationInMinutes"]
    else:
        out["deployment_duration_in_minutes"] = 0
    if "GrowthType" in data:
        import aws_sdk_appconfig.types.growth_type

        out["growth_type"] = aws_sdk_appconfig.types.growth_type.deserialize_json(
            data["GrowthType"]
        )
    if "GrowthFactor" in data:
        out["growth_factor"] = data["GrowthFactor"]
    if "FinalBakeTimeInMinutes" in data:
        out["final_bake_time_in_minutes"] = data["FinalBakeTimeInMinutes"]
    else:
        out["final_bake_time_in_minutes"] = 0
    if "ReplicateTo" in data:
        import aws_sdk_appconfig.types.replicate_to

        out["replicate_to"] = aws_sdk_appconfig.types.replicate_to.deserialize_json(
            data["ReplicateTo"]
        )
    return out
