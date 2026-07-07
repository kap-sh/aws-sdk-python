"""Generated from Smithy shape ``com.amazonaws.appconfig#CreateDeploymentStrategyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appconfig.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.description
    import aws_sdk_appconfig.types.growth_factor
    import aws_sdk_appconfig.types.growth_type
    import aws_sdk_appconfig.types.minutes_between0_and24_hours
    import aws_sdk_appconfig.types.name
    import aws_sdk_appconfig.types.replicate_to
    import aws_sdk_appconfig.types.tag_map


class CreateDeploymentStrategyRequest(TypedDict, closed=True):
    name: "aws_sdk_appconfig.types.name.Name"
    """<p>A name for the deployment strategy.</p>"""
    description: NotRequired["aws_sdk_appconfig.types.description.Description"]
    """<p>A description of the deployment strategy.</p>"""
    deployment_duration_in_minutes: (
        "aws_sdk_appconfig.types.minutes_between0_and24_hours.MinutesBetween0And24Hours"
    )
    """<p>Total amount of time for a deployment to last.</p>"""
    final_bake_time_in_minutes: (
        "aws_sdk_appconfig.types.minutes_between0_and24_hours.MinutesBetween0And24Hours"
    )
    r"""<p>Specifies the amount of time AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete. If an alarm is triggered during this time, AppConfig rolls back the deployment. You must configure permissions for AppConfig to roll back based on CloudWatch alarms. For more information, see <a href=\"https://docs.aws.amazon.com/appconfig/latest/userguide/getting-started-with-appconfig-cloudwatch-alarms-permissions.html\">Configuring permissions for rollback based on Amazon CloudWatch alarms</a> in the <i>AppConfig User Guide</i>.</p>"""
    growth_factor: "aws_sdk_appconfig.types.growth_factor.GrowthFactor"
    """<p>The percentage of targets to receive a deployed configuration during each interval.</p>"""
    growth_type: NotRequired["aws_sdk_appconfig.types.growth_type.GrowthType"]
    """<p>The algorithm used to define how percentage grows over time. AppConfig supports the following growth types:</p> <p> <b>Linear</b>: For this type, AppConfig processes the deployment by dividing the total number of targets by the value specified for <code>Step percentage</code>. For example, a linear deployment that uses a <code>Step percentage</code> of 10 deploys the configuration to 10 percent of the hosts. After those deployments are complete, the system deploys the configuration to the next 10 percent. This continues until 100% of the targets have successfully received the configuration.</p> <p> <b>Exponential</b>: For this type, AppConfig processes the deployment exponentially using the following formula: <code>G*(2^N)</code>. In this formula, <code>G</code> is the growth factor specified by the user and <code>N</code> is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows:</p> <p> <code>2*(2^0)</code> </p> <p> <code>2*(2^1)</code> </p> <p> <code>2*(2^2)</code> </p> <p>Expressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets.</p>"""
    replicate_to: NotRequired["aws_sdk_appconfig.types.replicate_to.ReplicateTo"]
    """<p>Save the deployment strategy to a Systems Manager (SSM) document.</p>"""
    tags: NotRequired["aws_sdk_appconfig.types.tag_map.TagMap"]
    """<p>Metadata to assign to the deployment strategy. Tags help organize and categorize your AppConfig resources. Each tag consists of a key and an optional value, both of which you define.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDeploymentStrategyRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    out["DeploymentDurationInMinutes"] = value["deployment_duration_in_minutes"]
    out["FinalBakeTimeInMinutes"] = value.get("final_bake_time_in_minutes", 0)
    out["GrowthFactor"] = value["growth_factor"]
    if "growth_type" in value:
        import aws_sdk_appconfig.types.growth_type

        out["GrowthType"] = aws_sdk_appconfig.types.growth_type.serialize_json(
            value["growth_type"]
        )
    if "replicate_to" in value:
        import aws_sdk_appconfig.types.replicate_to

        out["ReplicateTo"] = aws_sdk_appconfig.types.replicate_to.serialize_json(
            value["replicate_to"]
        )
    if "tags" in value:
        import aws_sdk_appconfig.types.tag_map

        out["Tags"] = aws_sdk_appconfig.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDeploymentStrategyRequest:
    out: CreateDeploymentStrategyRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateDeploymentStrategyRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "DeploymentDurationInMinutes" in data:
        out["deployment_duration_in_minutes"] = data["DeploymentDurationInMinutes"]
    else:
        raise DeserializationError(
            "CreateDeploymentStrategyRequest.deployment_duration_in_minutes required"
        )
    if "FinalBakeTimeInMinutes" in data:
        out["final_bake_time_in_minutes"] = data["FinalBakeTimeInMinutes"]
    else:
        out["final_bake_time_in_minutes"] = 0
    if "GrowthFactor" in data:
        out["growth_factor"] = data["GrowthFactor"]
    else:
        raise DeserializationError(
            "CreateDeploymentStrategyRequest.growth_factor required"
        )
    if "GrowthType" in data:
        import aws_sdk_appconfig.types.growth_type

        out["growth_type"] = aws_sdk_appconfig.types.growth_type.deserialize_json(
            data["GrowthType"]
        )
    if "ReplicateTo" in data:
        import aws_sdk_appconfig.types.replicate_to

        out["replicate_to"] = aws_sdk_appconfig.types.replicate_to.deserialize_json(
            data["ReplicateTo"]
        )
    if "Tags" in data:
        import aws_sdk_appconfig.types.tag_map

        out["tags"] = aws_sdk_appconfig.types.tag_map.deserialize_json(data["Tags"])
    return out
