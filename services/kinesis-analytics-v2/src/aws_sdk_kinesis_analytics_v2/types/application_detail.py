"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_configuration_description
    import aws_sdk_kinesis_analytics_v2.types.application_description
    import aws_sdk_kinesis_analytics_v2.types.application_maintenance_configuration_description
    import aws_sdk_kinesis_analytics_v2.types.application_mode
    import aws_sdk_kinesis_analytics_v2.types.application_name
    import aws_sdk_kinesis_analytics_v2.types.application_status
    import aws_sdk_kinesis_analytics_v2.types.application_version_id
    import aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions
    import aws_sdk_kinesis_analytics_v2.types.conditional_token
    import aws_sdk_kinesis_analytics_v2.types.resource_arn
    import aws_sdk_kinesis_analytics_v2.types.role_arn
    import aws_sdk_kinesis_analytics_v2.types.runtime_environment
    import aws_sdk_kinesis_analytics_v2.types.timestamp


class ApplicationDetail(TypedDict, closed=True):
    application_arn: "aws_sdk_kinesis_analytics_v2.types.resource_arn.ResourceARN"
    """<p>The ARN of the application.</p>"""
    application_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_description.ApplicationDescription"
    ]
    """<p>The description of the application.</p>"""
    application_name: (
        "aws_sdk_kinesis_analytics_v2.types.application_name.ApplicationName"
    )
    """<p>The name of the application.</p>"""
    runtime_environment: (
        "aws_sdk_kinesis_analytics_v2.types.runtime_environment.RuntimeEnvironment"
    )
    """<p>The runtime environment for the application.</p>"""
    service_execution_role: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.role_arn.RoleARN"
    ]
    """<p>Specifies the IAM role that the application uses to access external resources.</p>"""
    application_status: (
        "aws_sdk_kinesis_analytics_v2.types.application_status.ApplicationStatus"
    )
    """<p>The status of the application.</p>"""
    application_version_id: (
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    )
    """<p>Provides the current application version. Managed Service for Apache Flink updates the <code>ApplicationVersionId</code> each time you update the application.</p>"""
    create_timestamp: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.timestamp.Timestamp"
    ]
    """<p>The current timestamp when the application was created.</p>"""
    last_update_timestamp: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.timestamp.Timestamp"
    ]
    """<p>The current timestamp when the application was last updated.</p>"""
    application_configuration_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_configuration_description.ApplicationConfigurationDescription"
    ]
    """<p>Describes details about the application code and starting parameters for a Managed Service for Apache Flink application.</p>"""
    cloud_watch_logging_option_descriptions: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions.CloudWatchLoggingOptionDescriptions"
    ]
    """<p>Describes the application Amazon CloudWatch logging options.</p>"""
    application_maintenance_configuration_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_maintenance_configuration_description.ApplicationMaintenanceConfigurationDescription"
    ]
    """<p>The details of the maintenance configuration for the application.</p>"""
    application_version_updated_from: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>The previous application version before the latest application update. <a>RollbackApplication</a> reverts the application to this version.</p>"""
    application_version_rolled_back_from: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>If you reverted the application using <a>RollbackApplication</a>, the application version when <code>RollbackApplication</code> was called.</p>"""
    application_version_create_timestamp: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.timestamp.Timestamp"
    ]
    """<p>The timestamp that indicates when the application version was created.</p>"""
    conditional_token: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.conditional_token.ConditionalToken"
    ]
    """<p>A value you use to implement strong concurrency for application updates.</p>"""
    application_version_rolled_back_to: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    ]
    """<p>The version to which you want to roll back the application.</p>"""
    application_mode: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_mode.ApplicationMode"
    ]
    """<p>To create a Managed Service for Apache Flink Studio notebook, you must set the mode to <code>INTERACTIVE</code>. However, for a Managed Service for Apache Flink application, the mode is optional.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationDetail) -> dict:
    out: dict = {}
    out["ApplicationARN"] = value["application_arn"]
    if "application_description" in value:
        out["ApplicationDescription"] = value["application_description"]
    out["ApplicationName"] = value["application_name"]
    import aws_sdk_kinesis_analytics_v2.types.runtime_environment

    out["RuntimeEnvironment"] = (
        aws_sdk_kinesis_analytics_v2.types.runtime_environment.serialize_aws_json_1_1(
            value["runtime_environment"]
        )
    )
    if "service_execution_role" in value:
        out["ServiceExecutionRole"] = value["service_execution_role"]
    import aws_sdk_kinesis_analytics_v2.types.application_status

    out["ApplicationStatus"] = (
        aws_sdk_kinesis_analytics_v2.types.application_status.serialize_aws_json_1_1(
            value["application_status"]
        )
    )
    out["ApplicationVersionId"] = value["application_version_id"]
    if "create_timestamp" in value:
        import aws_sdk_kinesis_analytics_v2.types.timestamp

        out["CreateTimestamp"] = (
            aws_sdk_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
                value["create_timestamp"]
            )
        )
    if "last_update_timestamp" in value:
        import aws_sdk_kinesis_analytics_v2.types.timestamp

        out["LastUpdateTimestamp"] = (
            aws_sdk_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
                value["last_update_timestamp"]
            )
        )
    if "application_configuration_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_configuration_description

        out["ApplicationConfigurationDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.application_configuration_description.serialize_aws_json_1_1(
                value["application_configuration_description"]
            )
        )
    if "cloud_watch_logging_option_descriptions" in value:
        import aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions

        out["CloudWatchLoggingOptionDescriptions"] = (
            aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions.serialize_aws_json_1_1(
                value["cloud_watch_logging_option_descriptions"]
            )
        )
    if "application_maintenance_configuration_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_maintenance_configuration_description

        out["ApplicationMaintenanceConfigurationDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.application_maintenance_configuration_description.serialize_aws_json_1_1(
                value["application_maintenance_configuration_description"]
            )
        )
    if "application_version_updated_from" in value:
        out["ApplicationVersionUpdatedFrom"] = value["application_version_updated_from"]
    if "application_version_rolled_back_from" in value:
        out["ApplicationVersionRolledBackFrom"] = value[
            "application_version_rolled_back_from"
        ]
    if "application_version_create_timestamp" in value:
        import aws_sdk_kinesis_analytics_v2.types.timestamp

        out["ApplicationVersionCreateTimestamp"] = (
            aws_sdk_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
                value["application_version_create_timestamp"]
            )
        )
    if "conditional_token" in value:
        out["ConditionalToken"] = value["conditional_token"]
    if "application_version_rolled_back_to" in value:
        out["ApplicationVersionRolledBackTo"] = value[
            "application_version_rolled_back_to"
        ]
    if "application_mode" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_mode

        out["ApplicationMode"] = (
            aws_sdk_kinesis_analytics_v2.types.application_mode.serialize_aws_json_1_1(
                value["application_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationDetail:
    out: ApplicationDetail = {}  # type: ignore[typeddict-item]
    if "ApplicationARN" in data:
        out["application_arn"] = data["ApplicationARN"]
    else:
        raise DeserializationError("ApplicationDetail.application_arn required")
    if "ApplicationDescription" in data:
        out["application_description"] = data["ApplicationDescription"]
    if "ApplicationName" in data:
        out["application_name"] = data["ApplicationName"]
    else:
        raise DeserializationError("ApplicationDetail.application_name required")
    if "RuntimeEnvironment" in data:
        import aws_sdk_kinesis_analytics_v2.types.runtime_environment

        out["runtime_environment"] = (
            aws_sdk_kinesis_analytics_v2.types.runtime_environment.deserialize_aws_json_1_1(
                data["RuntimeEnvironment"]
            )
        )
    else:
        raise DeserializationError("ApplicationDetail.runtime_environment required")
    if "ServiceExecutionRole" in data:
        out["service_execution_role"] = data["ServiceExecutionRole"]
    if "ApplicationStatus" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_status

        out["application_status"] = (
            aws_sdk_kinesis_analytics_v2.types.application_status.deserialize_aws_json_1_1(
                data["ApplicationStatus"]
            )
        )
    else:
        raise DeserializationError("ApplicationDetail.application_status required")
    if "ApplicationVersionId" in data:
        out["application_version_id"] = data["ApplicationVersionId"]
    else:
        raise DeserializationError("ApplicationDetail.application_version_id required")
    if "CreateTimestamp" in data:
        import aws_sdk_kinesis_analytics_v2.types.timestamp

        out["create_timestamp"] = (
            aws_sdk_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["CreateTimestamp"]
            )
        )
    if "LastUpdateTimestamp" in data:
        import aws_sdk_kinesis_analytics_v2.types.timestamp

        out["last_update_timestamp"] = (
            aws_sdk_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["LastUpdateTimestamp"]
            )
        )
    if "ApplicationConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_configuration_description

        out["application_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.application_configuration_description.deserialize_aws_json_1_1(
                data["ApplicationConfigurationDescription"]
            )
        )
    if "CloudWatchLoggingOptionDescriptions" in data:
        import aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions

        out["cloud_watch_logging_option_descriptions"] = (
            aws_sdk_kinesis_analytics_v2.types.cloud_watch_logging_option_descriptions.deserialize_aws_json_1_1(
                data["CloudWatchLoggingOptionDescriptions"]
            )
        )
    if "ApplicationMaintenanceConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_maintenance_configuration_description

        out["application_maintenance_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.application_maintenance_configuration_description.deserialize_aws_json_1_1(
                data["ApplicationMaintenanceConfigurationDescription"]
            )
        )
    if "ApplicationVersionUpdatedFrom" in data:
        out["application_version_updated_from"] = data["ApplicationVersionUpdatedFrom"]
    if "ApplicationVersionRolledBackFrom" in data:
        out["application_version_rolled_back_from"] = data[
            "ApplicationVersionRolledBackFrom"
        ]
    if "ApplicationVersionCreateTimestamp" in data:
        import aws_sdk_kinesis_analytics_v2.types.timestamp

        out["application_version_create_timestamp"] = (
            aws_sdk_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["ApplicationVersionCreateTimestamp"]
            )
        )
    if "ConditionalToken" in data:
        out["conditional_token"] = data["ConditionalToken"]
    if "ApplicationVersionRolledBackTo" in data:
        out["application_version_rolled_back_to"] = data[
            "ApplicationVersionRolledBackTo"
        ]
    if "ApplicationMode" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_mode

        out["application_mode"] = (
            aws_sdk_kinesis_analytics_v2.types.application_mode.deserialize_aws_json_1_1(
                data["ApplicationMode"]
            )
        )
    return out
