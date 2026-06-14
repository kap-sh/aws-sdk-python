"""Generated from Smithy shape ``com.amazonaws.apprunner#ObservabilityConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.app_runner_resource_arn
    import aws_sdk_apprunner.types.boolean
    import aws_sdk_apprunner.types.integer
    import aws_sdk_apprunner.types.observability_configuration_name
    import aws_sdk_apprunner.types.observability_configuration_status
    import aws_sdk_apprunner.types.timestamp
    import aws_sdk_apprunner.types.trace_configuration


class ObservabilityConfiguration(TypedDict):
    observability_configuration_arn: NotRequired[
        "aws_sdk_apprunner.types.app_runner_resource_arn.AppRunnerResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of this observability configuration.</p>"""
    observability_configuration_name: NotRequired[
        "aws_sdk_apprunner.types.observability_configuration_name.ObservabilityConfigurationName"
    ]
    """<p>The customer-provided observability configuration name. It can be used in multiple revisions of a configuration.</p>"""
    trace_configuration: NotRequired[
        "aws_sdk_apprunner.types.trace_configuration.TraceConfiguration"
    ]
    """<p>The configuration of the tracing feature within this observability configuration. If not specified, tracing isn't enabled.</p>"""
    observability_configuration_revision: "aws_sdk_apprunner.types.integer.Integer"
    r"""<p>The revision of this observability configuration. It's unique among all the active configurations (<code>\"Status\": \"ACTIVE\"</code>) that share the same <code>ObservabilityConfigurationName</code>.</p>"""
    latest: "aws_sdk_apprunner.types.boolean.Boolean"
    """<p>It's set to <code>true</code> for the configuration with the highest <code>Revision</code> among all configurations that share the same <code>ObservabilityConfigurationName</code>. It's set to <code>false</code> otherwise.</p>"""
    status: NotRequired[
        "aws_sdk_apprunner.types.observability_configuration_status.ObservabilityConfigurationStatus"
    ]
    """<p>The current state of the observability configuration. If the status of a configuration revision is <code>INACTIVE</code>, it was deleted and can't be used. Inactive configuration revisions are permanently removed some time after they are deleted.</p>"""
    created_at: NotRequired["aws_sdk_apprunner.types.timestamp.Timestamp"]
    """<p>The time when the observability configuration was created. It's in Unix time stamp format.</p>"""
    deleted_at: NotRequired["aws_sdk_apprunner.types.timestamp.Timestamp"]
    """<p>The time when the observability configuration was deleted. It's in Unix time stamp format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ObservabilityConfiguration) -> dict:
    out: dict = {}
    if "observability_configuration_arn" in value:
        out["ObservabilityConfigurationArn"] = value["observability_configuration_arn"]
    if "observability_configuration_name" in value:
        out["ObservabilityConfigurationName"] = value[
            "observability_configuration_name"
        ]
    if "trace_configuration" in value:
        import aws_sdk_apprunner.types.trace_configuration

        out["TraceConfiguration"] = (
            aws_sdk_apprunner.types.trace_configuration.serialize_aws_json_1_0(
                value["trace_configuration"]
            )
        )
    out["ObservabilityConfigurationRevision"] = value.get(
        "observability_configuration_revision", 0
    )
    out["Latest"] = value.get("latest", False)
    if "status" in value:
        import aws_sdk_apprunner.types.observability_configuration_status

        out["Status"] = (
            aws_sdk_apprunner.types.observability_configuration_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
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
    return out


def deserialize_aws_json_1_0(data: dict) -> ObservabilityConfiguration:
    out: ObservabilityConfiguration = {}  # type: ignore[typeddict-item]
    if "ObservabilityConfigurationArn" in data:
        out["observability_configuration_arn"] = data["ObservabilityConfigurationArn"]
    if "ObservabilityConfigurationName" in data:
        out["observability_configuration_name"] = data["ObservabilityConfigurationName"]
    if "TraceConfiguration" in data:
        import aws_sdk_apprunner.types.trace_configuration

        out["trace_configuration"] = (
            aws_sdk_apprunner.types.trace_configuration.deserialize_aws_json_1_0(
                data["TraceConfiguration"]
            )
        )
    if "ObservabilityConfigurationRevision" in data:
        out["observability_configuration_revision"] = data[
            "ObservabilityConfigurationRevision"
        ]
    else:
        out["observability_configuration_revision"] = 0
    if "Latest" in data:
        out["latest"] = data["Latest"]
    else:
        out["latest"] = False
    if "Status" in data:
        import aws_sdk_apprunner.types.observability_configuration_status

        out["status"] = (
            aws_sdk_apprunner.types.observability_configuration_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
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
    return out
