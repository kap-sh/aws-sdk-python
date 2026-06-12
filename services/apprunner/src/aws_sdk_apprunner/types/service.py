"""Generated from Smithy shape ``com.amazonaws.apprunner#Service``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn
    import aws_sdk_apprunner.types.auto_scaling_configuration_summary
    import aws_sdk_apprunner.types.encryption_configuration
    import aws_sdk_apprunner.types.health_check_configuration
    import aws_sdk_apprunner.types.instance_configuration
    import aws_sdk_apprunner.types.network_configuration
    import aws_sdk_apprunner.types.service_id
    import aws_sdk_apprunner.types.service_name
    import aws_sdk_apprunner.types.service_observability_configuration
    import aws_sdk_apprunner.types.service_status
    import aws_sdk_apprunner.types.source_configuration
    import aws_sdk_apprunner.types.string
    import aws_sdk_apprunner.types.timestamp


class Service(TypedDict):
    service_name: "aws_sdk_apprunner.types.service_name.ServiceName"
    """<p>The customer-provided service name.</p>"""
    service_id: "aws_sdk_apprunner.types.service_id.ServiceId"
    """<p>An ID that App Runner generated for this service. It's unique within the Amazon Web Services Region.</p>"""
    service_arn: "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    """<p>The Amazon Resource Name (ARN) of this service.</p>"""
    service_url: NotRequired["aws_sdk_apprunner.types.string.String"]
    """<p>A subdomain URL that App Runner generated for this service. You can use this URL to access your service web application.</p>"""
    created_at: "aws_sdk_apprunner.types.timestamp.Timestamp"
    """<p>The time when the App Runner service was created. It's in the Unix time stamp format.</p>"""
    updated_at: "aws_sdk_apprunner.types.timestamp.Timestamp"
    """<p>The time when the App Runner service was last updated at. It's in the Unix time stamp format.</p>"""
    deleted_at: NotRequired["aws_sdk_apprunner.types.timestamp.Timestamp"]
    """<p>The time when the App Runner service was deleted. It's in the Unix time stamp format.</p>"""
    status: "aws_sdk_apprunner.types.service_status.ServiceStatus"
    """<p>The current state of the App Runner service. These particular values mean the following.</p> <ul> <li> <p> <code>CREATE_FAILED</code> – The service failed to create. The failed service isn't usable, and still counts towards your service quota. To troubleshoot this failure, read the failure events and logs, change any parameters that need to be fixed, and rebuild your service using <code>UpdateService</code>.</p> </li> <li> <p> <code>DELETE_FAILED</code> – The service failed to delete and can't be successfully recovered. Retry the service deletion call to ensure that all related resources are removed.</p> </li> </ul>"""
    source_configuration: (
        "aws_sdk_apprunner.types.source_configuration.SourceConfiguration"
    )
    """<p>The source deployed to the App Runner service. It can be a code or an image repository.</p>"""
    instance_configuration: (
        "aws_sdk_apprunner.types.instance_configuration.InstanceConfiguration"
    )
    """<p>The runtime configuration of instances (scaling units) of this service.</p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_apprunner.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption key that App Runner uses to encrypt the service logs and the copy of the source repository that App Runner maintains for the service. It can be either a customer-provided encryption key or an Amazon Web Services managed key.</p>"""
    health_check_configuration: NotRequired[
        "aws_sdk_apprunner.types.health_check_configuration.HealthCheckConfiguration"
    ]
    """<p>The settings for the health check that App Runner performs to monitor the health of this service.</p>"""
    auto_scaling_configuration_summary: "aws_sdk_apprunner.types.auto_scaling_configuration_summary.AutoScalingConfigurationSummary"
    """<p>Summary information for the App Runner automatic scaling configuration resource that's associated with this service.</p>"""
    network_configuration: (
        "aws_sdk_apprunner.types.network_configuration.NetworkConfiguration"
    )
    """<p>Configuration settings related to network traffic of the web application that this service runs.</p>"""
    observability_configuration: NotRequired[
        "aws_sdk_apprunner.types.service_observability_configuration.ServiceObservabilityConfiguration"
    ]
    """<p>The observability configuration of this service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Service) -> dict:
    out: dict = {}
    out["ServiceName"] = value["service_name"]
    out["ServiceId"] = value["service_id"]
    out["ServiceArn"] = value["service_arn"]
    if "service_url" in value:
        out["ServiceUrl"] = value["service_url"]
    import aws_sdk_apprunner.types.timestamp

    out["CreatedAt"] = aws_sdk_apprunner.types.timestamp.serialize_aws_json_1_0(
        value["created_at"]
    )
    import aws_sdk_apprunner.types.timestamp

    out["UpdatedAt"] = aws_sdk_apprunner.types.timestamp.serialize_aws_json_1_0(
        value["updated_at"]
    )
    if "deleted_at" in value:
        import aws_sdk_apprunner.types.timestamp

        out["DeletedAt"] = aws_sdk_apprunner.types.timestamp.serialize_aws_json_1_0(
            value["deleted_at"]
        )
    import aws_sdk_apprunner.types.service_status

    out["Status"] = aws_sdk_apprunner.types.service_status.serialize_aws_json_1_0(
        value["status"]
    )
    import aws_sdk_apprunner.types.source_configuration

    out["SourceConfiguration"] = (
        aws_sdk_apprunner.types.source_configuration.serialize_aws_json_1_0(
            value["source_configuration"]
        )
    )
    import aws_sdk_apprunner.types.instance_configuration

    out["InstanceConfiguration"] = (
        aws_sdk_apprunner.types.instance_configuration.serialize_aws_json_1_0(
            value["instance_configuration"]
        )
    )
    if "encryption_configuration" in value:
        import aws_sdk_apprunner.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            aws_sdk_apprunner.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    if "health_check_configuration" in value:
        import aws_sdk_apprunner.types.health_check_configuration

        out["HealthCheckConfiguration"] = (
            aws_sdk_apprunner.types.health_check_configuration.serialize_aws_json_1_0(
                value["health_check_configuration"]
            )
        )
    import aws_sdk_apprunner.types.auto_scaling_configuration_summary

    out["AutoScalingConfigurationSummary"] = (
        aws_sdk_apprunner.types.auto_scaling_configuration_summary.serialize_aws_json_1_0(
            value["auto_scaling_configuration_summary"]
        )
    )
    import aws_sdk_apprunner.types.network_configuration

    out["NetworkConfiguration"] = (
        aws_sdk_apprunner.types.network_configuration.serialize_aws_json_1_0(
            value["network_configuration"]
        )
    )
    if "observability_configuration" in value:
        import aws_sdk_apprunner.types.service_observability_configuration

        out["ObservabilityConfiguration"] = (
            aws_sdk_apprunner.types.service_observability_configuration.serialize_aws_json_1_0(
                value["observability_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Service:
    out: Service = {}  # type: ignore[typeddict-item]
    if "ServiceName" in data:
        out["service_name"] = data["ServiceName"]
    else:
        raise DeserializationError("Service.service_name required")
    if "ServiceId" in data:
        out["service_id"] = data["ServiceId"]
    else:
        raise DeserializationError("Service.service_id required")
    if "ServiceArn" in data:
        out["service_arn"] = data["ServiceArn"]
    else:
        raise DeserializationError("Service.service_arn required")
    if "ServiceUrl" in data:
        out["service_url"] = data["ServiceUrl"]
    if "CreatedAt" in data:
        import aws_sdk_apprunner.types.timestamp

        out["created_at"] = aws_sdk_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    else:
        raise DeserializationError("Service.created_at required")
    if "UpdatedAt" in data:
        import aws_sdk_apprunner.types.timestamp

        out["updated_at"] = aws_sdk_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["UpdatedAt"]
        )
    else:
        raise DeserializationError("Service.updated_at required")
    if "DeletedAt" in data:
        import aws_sdk_apprunner.types.timestamp

        out["deleted_at"] = aws_sdk_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["DeletedAt"]
        )
    if "Status" in data:
        import aws_sdk_apprunner.types.service_status

        out["status"] = aws_sdk_apprunner.types.service_status.deserialize_aws_json_1_0(
            data["Status"]
        )
    else:
        raise DeserializationError("Service.status required")
    if "SourceConfiguration" in data:
        import aws_sdk_apprunner.types.source_configuration

        out["source_configuration"] = (
            aws_sdk_apprunner.types.source_configuration.deserialize_aws_json_1_0(
                data["SourceConfiguration"]
            )
        )
    else:
        raise DeserializationError("Service.source_configuration required")
    if "InstanceConfiguration" in data:
        import aws_sdk_apprunner.types.instance_configuration

        out["instance_configuration"] = (
            aws_sdk_apprunner.types.instance_configuration.deserialize_aws_json_1_0(
                data["InstanceConfiguration"]
            )
        )
    else:
        raise DeserializationError("Service.instance_configuration required")
    if "EncryptionConfiguration" in data:
        import aws_sdk_apprunner.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_apprunner.types.encryption_configuration.deserialize_aws_json_1_0(
                data["EncryptionConfiguration"]
            )
        )
    if "HealthCheckConfiguration" in data:
        import aws_sdk_apprunner.types.health_check_configuration

        out["health_check_configuration"] = (
            aws_sdk_apprunner.types.health_check_configuration.deserialize_aws_json_1_0(
                data["HealthCheckConfiguration"]
            )
        )
    if "AutoScalingConfigurationSummary" in data:
        import aws_sdk_apprunner.types.auto_scaling_configuration_summary

        out["auto_scaling_configuration_summary"] = (
            aws_sdk_apprunner.types.auto_scaling_configuration_summary.deserialize_aws_json_1_0(
                data["AutoScalingConfigurationSummary"]
            )
        )
    else:
        raise DeserializationError(
            "Service.auto_scaling_configuration_summary required"
        )
    if "NetworkConfiguration" in data:
        import aws_sdk_apprunner.types.network_configuration

        out["network_configuration"] = (
            aws_sdk_apprunner.types.network_configuration.deserialize_aws_json_1_0(
                data["NetworkConfiguration"]
            )
        )
    else:
        raise DeserializationError("Service.network_configuration required")
    if "ObservabilityConfiguration" in data:
        import aws_sdk_apprunner.types.service_observability_configuration

        out["observability_configuration"] = (
            aws_sdk_apprunner.types.service_observability_configuration.deserialize_aws_json_1_0(
                data["ObservabilityConfiguration"]
            )
        )
    return out
