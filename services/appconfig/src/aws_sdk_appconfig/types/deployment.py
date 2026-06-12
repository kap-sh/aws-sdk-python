"""Generated from Smithy shape ``com.amazonaws.appconfig#Deployment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.applied_extensions
    import aws_sdk_appconfig.types.arn
    import aws_sdk_appconfig.types.deployment_events
    import aws_sdk_appconfig.types.deployment_state
    import aws_sdk_appconfig.types.description
    import aws_sdk_appconfig.types.growth_type
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.integer
    import aws_sdk_appconfig.types.iso8601_date_time
    import aws_sdk_appconfig.types.kms_key_identifier
    import aws_sdk_appconfig.types.minutes_between0_and24_hours
    import aws_sdk_appconfig.types.name
    import aws_sdk_appconfig.types.percentage
    import aws_sdk_appconfig.types.uri
    import aws_sdk_appconfig.types.version
    import aws_sdk_appconfig.types.version_label


class Deployment(TypedDict):
    application_id: NotRequired["aws_sdk_appconfig.types.id.Id"]
    """<p>The ID of the application that was deployed.</p>"""
    environment_id: NotRequired["aws_sdk_appconfig.types.id.Id"]
    """<p>The ID of the environment that was deployed.</p>"""
    deployment_strategy_id: NotRequired["aws_sdk_appconfig.types.id.Id"]
    """<p>The ID of the deployment strategy that was deployed.</p>"""
    configuration_profile_id: NotRequired["aws_sdk_appconfig.types.id.Id"]
    """<p>The ID of the configuration profile that was deployed.</p>"""
    deployment_number: "aws_sdk_appconfig.types.integer.Integer"
    """<p>The sequence number of the deployment.</p>"""
    configuration_name: NotRequired["aws_sdk_appconfig.types.name.Name"]
    """<p>The name of the configuration.</p>"""
    configuration_location_uri: NotRequired["aws_sdk_appconfig.types.uri.Uri"]
    """<p>Information about the source location of the configuration.</p>"""
    configuration_version: NotRequired["aws_sdk_appconfig.types.version.Version"]
    """<p>The configuration version that was deployed.</p>"""
    description: NotRequired["aws_sdk_appconfig.types.description.Description"]
    """<p>The description of the deployment.</p>"""
    deployment_duration_in_minutes: (
        "aws_sdk_appconfig.types.minutes_between0_and24_hours.MinutesBetween0And24Hours"
    )
    """<p>Total amount of time the deployment lasted.</p>"""
    growth_type: NotRequired["aws_sdk_appconfig.types.growth_type.GrowthType"]
    """<p>The algorithm used to define how percentage grew over time.</p>"""
    growth_factor: NotRequired["aws_sdk_appconfig.types.percentage.Percentage"]
    """<p>The percentage of targets to receive a deployed configuration during each interval.</p>"""
    final_bake_time_in_minutes: (
        "aws_sdk_appconfig.types.minutes_between0_and24_hours.MinutesBetween0And24Hours"
    )
    """<p>The amount of time that AppConfig monitored for alarms before considering the deployment to be complete and no longer eligible for automatic rollback.</p>"""
    state: NotRequired["aws_sdk_appconfig.types.deployment_state.DeploymentState"]
    """<p>The state of the deployment.</p>"""
    event_log: NotRequired["aws_sdk_appconfig.types.deployment_events.DeploymentEvents"]
    """<p>A list containing all events related to a deployment. The most recent events are displayed first.</p>"""
    percentage_complete: NotRequired["aws_sdk_appconfig.types.percentage.Percentage"]
    """<p>The percentage of targets for which the deployment is available.</p>"""
    started_at: NotRequired["aws_sdk_appconfig.types.iso8601_date_time.Iso8601DateTime"]
    """<p>The time the deployment started.</p>"""
    completed_at: NotRequired[
        "aws_sdk_appconfig.types.iso8601_date_time.Iso8601DateTime"
    ]
    """<p>The time the deployment completed. </p>"""
    applied_extensions: NotRequired[
        "aws_sdk_appconfig.types.applied_extensions.AppliedExtensions"
    ]
    """<p>A list of extensions that were processed as part of the deployment. The extensions that were previously associated to the configuration profile, environment, or the application when <code>StartDeployment</code> was called.</p>"""
    kms_key_arn: NotRequired["aws_sdk_appconfig.types.arn.Arn"]
    """<p>The Amazon Resource Name of the Key Management Service key used to encrypt configuration data. You can encrypt secrets stored in Secrets Manager, Amazon Simple Storage Service (Amazon S3) objects encrypted with SSE-KMS, or secure string parameters stored in Amazon Web Services Systems Manager Parameter Store. </p>"""
    kms_key_identifier: NotRequired[
        "aws_sdk_appconfig.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    """<p>The Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.</p>"""
    version_label: NotRequired["aws_sdk_appconfig.types.version_label.VersionLabel"]
    """<p>A user-defined label for an AppConfig hosted configuration version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Deployment) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "environment_id" in value:
        out["EnvironmentId"] = value["environment_id"]
    if "deployment_strategy_id" in value:
        out["DeploymentStrategyId"] = value["deployment_strategy_id"]
    if "configuration_profile_id" in value:
        out["ConfigurationProfileId"] = value["configuration_profile_id"]
    out["DeploymentNumber"] = value.get("deployment_number", 0)
    if "configuration_name" in value:
        out["ConfigurationName"] = value["configuration_name"]
    if "configuration_location_uri" in value:
        out["ConfigurationLocationUri"] = value["configuration_location_uri"]
    if "configuration_version" in value:
        out["ConfigurationVersion"] = value["configuration_version"]
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
    if "state" in value:
        import aws_sdk_appconfig.types.deployment_state

        out["State"] = aws_sdk_appconfig.types.deployment_state.serialize_json(
            value["state"]
        )
    if "event_log" in value:
        import aws_sdk_appconfig.types.deployment_events

        out["EventLog"] = aws_sdk_appconfig.types.deployment_events.serialize_json(
            value["event_log"]
        )
    if "percentage_complete" in value:
        out["PercentageComplete"] = value["percentage_complete"]
    if "started_at" in value:
        import aws_sdk_appconfig.types.iso8601_date_time

        out["StartedAt"] = aws_sdk_appconfig.types.iso8601_date_time.serialize_json(
            value["started_at"]
        )
    if "completed_at" in value:
        import aws_sdk_appconfig.types.iso8601_date_time

        out["CompletedAt"] = aws_sdk_appconfig.types.iso8601_date_time.serialize_json(
            value["completed_at"]
        )
    if "applied_extensions" in value:
        import aws_sdk_appconfig.types.applied_extensions

        out["AppliedExtensions"] = (
            aws_sdk_appconfig.types.applied_extensions.serialize_json(
                value["applied_extensions"]
            )
        )
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    if "version_label" in value:
        out["VersionLabel"] = value["version_label"]
    return out


def deserialize_json(data: dict) -> Deployment:
    out: Deployment = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "EnvironmentId" in data:
        out["environment_id"] = data["EnvironmentId"]
    if "DeploymentStrategyId" in data:
        out["deployment_strategy_id"] = data["DeploymentStrategyId"]
    if "ConfigurationProfileId" in data:
        out["configuration_profile_id"] = data["ConfigurationProfileId"]
    if "DeploymentNumber" in data:
        out["deployment_number"] = data["DeploymentNumber"]
    else:
        out["deployment_number"] = 0
    if "ConfigurationName" in data:
        out["configuration_name"] = data["ConfigurationName"]
    if "ConfigurationLocationUri" in data:
        out["configuration_location_uri"] = data["ConfigurationLocationUri"]
    if "ConfigurationVersion" in data:
        out["configuration_version"] = data["ConfigurationVersion"]
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
    if "State" in data:
        import aws_sdk_appconfig.types.deployment_state

        out["state"] = aws_sdk_appconfig.types.deployment_state.deserialize_json(
            data["State"]
        )
    if "EventLog" in data:
        import aws_sdk_appconfig.types.deployment_events

        out["event_log"] = aws_sdk_appconfig.types.deployment_events.deserialize_json(
            data["EventLog"]
        )
    if "PercentageComplete" in data:
        out["percentage_complete"] = data["PercentageComplete"]
    if "StartedAt" in data:
        import aws_sdk_appconfig.types.iso8601_date_time

        out["started_at"] = aws_sdk_appconfig.types.iso8601_date_time.deserialize_json(
            data["StartedAt"]
        )
    if "CompletedAt" in data:
        import aws_sdk_appconfig.types.iso8601_date_time

        out["completed_at"] = (
            aws_sdk_appconfig.types.iso8601_date_time.deserialize_json(
                data["CompletedAt"]
            )
        )
    if "AppliedExtensions" in data:
        import aws_sdk_appconfig.types.applied_extensions

        out["applied_extensions"] = (
            aws_sdk_appconfig.types.applied_extensions.deserialize_json(
                data["AppliedExtensions"]
            )
        )
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if "KmsKeyIdentifier" in data:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    if "VersionLabel" in data:
        out["version_label"] = data["VersionLabel"]
    return out
