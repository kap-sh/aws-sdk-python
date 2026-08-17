"""Generated from Smithy shape ``com.amazonaws.ecs#ExecuteCommandConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.execute_command_log_configuration
    import capo_ecs.types.execute_command_logging
    import capo_ecs.types.string


class ExecuteCommandConfiguration(TypedDict, closed=True):
    kms_key_id: NotRequired["capo_ecs.types.string.String"]
    """<p>Specify an Key Management Service key ID to encrypt the data between the local client and the container.</p>"""
    logging: NotRequired["capo_ecs.types.execute_command_logging.ExecuteCommandLogging"]
    """<p>The log setting to use for redirecting logs for your execute command results. The following log settings are available.</p> <ul> <li> <p> <code>NONE</code>: The execute command session is not logged.</p> </li> <li> <p> <code>DEFAULT</code>: The <code>awslogs</code> configuration in the task definition is used. If no logging parameter is specified, it defaults to this value. If no <code>awslogs</code> log driver is configured in the task definition, the output won't be logged.</p> </li> <li> <p> <code>OVERRIDE</code>: Specify the logging details as a part of <code>logConfiguration</code>. If the <code>OVERRIDE</code> logging option is specified, the <code>logConfiguration</code> is required.</p> </li> </ul>"""
    log_configuration: NotRequired[
        "capo_ecs.types.execute_command_log_configuration.ExecuteCommandLogConfiguration"
    ]
    """<p>The log configuration for the results of the execute command actions. The logs can be sent to CloudWatch Logs or an Amazon S3 bucket. When <code>logging=OVERRIDE</code> is specified, a <code>logConfiguration</code> must be provided.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecuteCommandConfiguration) -> dict:
    out: dict = {}
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "logging" in value:
        import capo_ecs.types.execute_command_logging

        out["logging"] = capo_ecs.types.execute_command_logging.serialize_aws_json_1_1(
            value["logging"]
        )
    if "log_configuration" in value:
        import capo_ecs.types.execute_command_log_configuration

        out["logConfiguration"] = (
            capo_ecs.types.execute_command_log_configuration.serialize_aws_json_1_1(
                value["log_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecuteCommandConfiguration:
    out: ExecuteCommandConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("logging") is not None:
        import capo_ecs.types.execute_command_logging

        out["logging"] = (
            capo_ecs.types.execute_command_logging.deserialize_aws_json_1_1(
                data["logging"]
            )
        )
    if data.get("logConfiguration") is not None:
        import capo_ecs.types.execute_command_log_configuration

        out["log_configuration"] = (
            capo_ecs.types.execute_command_log_configuration.deserialize_aws_json_1_1(
                data["logConfiguration"]
            )
        )
    return out
