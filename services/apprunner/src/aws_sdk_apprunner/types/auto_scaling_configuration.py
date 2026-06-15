"""Generated from Smithy shape ``com.amazonaws.apprunner#AutoScalingConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn
    import aws_sdk_apprunner.types.auto_scaling_configuration_name
    import aws_sdk_apprunner.types.auto_scaling_configuration_revision
    import aws_sdk_apprunner.types.auto_scaling_configuration_status
    import aws_sdk_apprunner.types.has_associated_service
    import aws_sdk_apprunner.types.is_default
    import aws_sdk_apprunner.types.latest
    import aws_sdk_apprunner.types.max_concurrency
    import aws_sdk_apprunner.types.max_size
    import aws_sdk_apprunner.types.min_size
    import aws_sdk_apprunner.types.timestamp


class AutoScalingConfiguration(TypedDict):
    auto_scaling_configuration_arn: NotRequired[
        "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of this auto scaling configuration.</p>"""
    auto_scaling_configuration_name: NotRequired[
        "aws_sdk_apprunner.types.auto_scaling_configuration_name.AutoScalingConfigurationName"
    ]
    """<p>The customer-provided auto scaling configuration name. It can be used in multiple revisions of a configuration.</p>"""
    auto_scaling_configuration_revision: NotRequired[
        "aws_sdk_apprunner.types.auto_scaling_configuration_revision.AutoScalingConfigurationRevision"
    ]
    r"""<p>The revision of this auto scaling configuration. It's unique among all the active configurations (<code>\"Status\": \"ACTIVE\"</code>) that share the same <code>AutoScalingConfigurationName</code>.</p>"""
    latest: NotRequired["aws_sdk_apprunner.types.latest.Latest"]
    """<p>It's set to <code>true</code> for the configuration with the highest <code>Revision</code> among all configurations that share the same <code>AutoScalingConfigurationName</code>. It's set to <code>false</code> otherwise.</p>"""
    status: NotRequired[
        "aws_sdk_apprunner.types.auto_scaling_configuration_status.AutoScalingConfigurationStatus"
    ]
    """<p>The current state of the auto scaling configuration. If the status of a configuration revision is <code>INACTIVE</code>, it was deleted and can't be used. Inactive configuration revisions are permanently removed some time after they are deleted.</p>"""
    max_concurrency: NotRequired[
        "aws_sdk_apprunner.types.max_concurrency.MaxConcurrency"
    ]
    """<p>The maximum number of concurrent requests that an instance processes. If the number of concurrent requests exceeds this limit, App Runner scales the service up.</p>"""
    min_size: NotRequired["aws_sdk_apprunner.types.min_size.MinSize"]
    """<p>The minimum number of instances that App Runner provisions for a service. The service always has at least <code>MinSize</code> provisioned instances. Some of them actively serve traffic. The rest of them (provisioned and inactive instances) are a cost-effective compute capacity reserve and are ready to be quickly activated. You pay for memory usage of all the provisioned instances. You pay for CPU usage of only the active subset.</p> <p>App Runner temporarily doubles the number of provisioned instances during deployments, to maintain the same capacity for both old and new code.</p>"""
    max_size: NotRequired["aws_sdk_apprunner.types.max_size.MaxSize"]
    """<p>The maximum number of instances that a service scales up to. At most <code>MaxSize</code> instances actively serve traffic for your service.</p>"""
    created_at: NotRequired["aws_sdk_apprunner.types.timestamp.Timestamp"]
    """<p>The time when the auto scaling configuration was created. It's in Unix time stamp format.</p>"""
    deleted_at: NotRequired["aws_sdk_apprunner.types.timestamp.Timestamp"]
    """<p>The time when the auto scaling configuration was deleted. It's in Unix time stamp format.</p>"""
    has_associated_service: NotRequired[
        "aws_sdk_apprunner.types.has_associated_service.HasAssociatedService"
    ]
    """<p>Indicates if this auto scaling configuration has an App Runner service associated with it. A value of <code>true</code> indicates one or more services are associated. A value of <code>false</code> indicates no services are associated.</p>"""
    is_default: NotRequired["aws_sdk_apprunner.types.is_default.IsDefault"]
    """<p>Indicates if this auto scaling configuration should be used as the default for a new App Runner service that does not have an auto scaling configuration ARN specified during creation. Each account can have only one default <code>AutoScalingConfiguration</code> per region. The default <code>AutoScalingConfiguration</code> can be any revision under the same <code>AutoScalingConfigurationName</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutoScalingConfiguration) -> dict:
    out: dict = {}
    if "auto_scaling_configuration_arn" in value:
        out["AutoScalingConfigurationArn"] = value["auto_scaling_configuration_arn"]
    if "auto_scaling_configuration_name" in value:
        out["AutoScalingConfigurationName"] = value["auto_scaling_configuration_name"]
    if "auto_scaling_configuration_revision" in value:
        out["AutoScalingConfigurationRevision"] = value[
            "auto_scaling_configuration_revision"
        ]
    if "latest" in value:
        out["Latest"] = value["latest"]
    if "status" in value:
        import aws_sdk_apprunner.types.auto_scaling_configuration_status

        out["Status"] = (
            aws_sdk_apprunner.types.auto_scaling_configuration_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "max_concurrency" in value:
        out["MaxConcurrency"] = value["max_concurrency"]
    if "min_size" in value:
        out["MinSize"] = value["min_size"]
    if "max_size" in value:
        out["MaxSize"] = value["max_size"]
    if "created_at" in value:
        import aws_sdk_apprunner.types.timestamp

        out["CreatedAt"] = aws_sdk_apprunner.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "deleted_at" in value:
        import aws_sdk_apprunner.types.timestamp

        out["DeletedAt"] = aws_sdk_apprunner.types.timestamp.serialize_aws_json_1_0(
            value["deleted_at"]
        )
    if "has_associated_service" in value:
        out["HasAssociatedService"] = value["has_associated_service"]
    if "is_default" in value:
        out["IsDefault"] = value["is_default"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AutoScalingConfiguration:
    out: AutoScalingConfiguration = {}  # type: ignore[typeddict-item]
    if "AutoScalingConfigurationArn" in data:
        out["auto_scaling_configuration_arn"] = data["AutoScalingConfigurationArn"]
    if "AutoScalingConfigurationName" in data:
        out["auto_scaling_configuration_name"] = data["AutoScalingConfigurationName"]
    if "AutoScalingConfigurationRevision" in data:
        out["auto_scaling_configuration_revision"] = data[
            "AutoScalingConfigurationRevision"
        ]
    if "Latest" in data:
        out["latest"] = data["Latest"]
    if "Status" in data:
        import aws_sdk_apprunner.types.auto_scaling_configuration_status

        out["status"] = (
            aws_sdk_apprunner.types.auto_scaling_configuration_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "MaxConcurrency" in data:
        out["max_concurrency"] = data["MaxConcurrency"]
    if "MinSize" in data:
        out["min_size"] = data["MinSize"]
    if "MaxSize" in data:
        out["max_size"] = data["MaxSize"]
    if "CreatedAt" in data:
        import aws_sdk_apprunner.types.timestamp

        out["created_at"] = aws_sdk_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["CreatedAt"]
        )
    if "DeletedAt" in data:
        import aws_sdk_apprunner.types.timestamp

        out["deleted_at"] = aws_sdk_apprunner.types.timestamp.deserialize_aws_json_1_0(
            data["DeletedAt"]
        )
    if "HasAssociatedService" in data:
        out["has_associated_service"] = data["HasAssociatedService"]
    if "IsDefault" in data:
        out["is_default"] = data["IsDefault"]
    return out
