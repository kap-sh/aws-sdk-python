"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsClusterConfigurationExecuteCommandConfigurationDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_log_configuration_details
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsClusterConfigurationExecuteCommandConfigurationDetails(TypedDict):
    kms_key_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The identifier of the KMS key that is used to encrypt the data between the local client and the container.</p>"""
    log_configuration: NotRequired[
        "aws_sdk_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_log_configuration_details.AwsEcsClusterConfigurationExecuteCommandConfigurationLogConfigurationDetails"
    ]
    """<p>The log configuration for the results of the run command actions. Required if <code>Logging</code> is <code>NONE</code>.</p>"""
    logging: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The log setting to use for redirecting logs for run command results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsClusterConfigurationExecuteCommandConfigurationDetails,
) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "log_configuration" in value:
        import aws_sdk_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_log_configuration_details

        out["LogConfiguration"] = (
            aws_sdk_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_log_configuration_details.serialize_json(
                value["log_configuration"]
            )
        )
    if "logging" in value:
        out["Logging"] = value["logging"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsClusterConfigurationExecuteCommandConfigurationDetails:
    out: AwsEcsClusterConfigurationExecuteCommandConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "LogConfiguration" in data:
        import aws_sdk_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_log_configuration_details

        out["log_configuration"] = (
            aws_sdk_securityhub.types.aws_ecs_cluster_configuration_execute_command_configuration_log_configuration_details.deserialize_json(
                data["LogConfiguration"]
            )
        )
    if "Logging" in data:
        out["logging"] = data["Logging"]
    return out
