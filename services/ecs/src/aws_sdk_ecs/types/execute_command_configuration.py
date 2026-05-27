"""Generated from Smithy shape ``com.amazonaws.ecs#ExecuteCommandConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.execute_command_log_configuration
    import aws_sdk_ecs.types.execute_command_logging
    import aws_sdk_ecs.types.string


class ExecuteCommandConfiguration(TypedDict):
    kms_key_id: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Specify an Key Management Service key ID to encrypt the data between the local client and the container.</p>"""
    logging: NotRequired[
        "aws_sdk_ecs.types.execute_command_logging.ExecuteCommandLogging"
    ]
    """<p>The log setting to use for redirecting logs for your execute command results. The following log settings are available.</p> <ul> <li> <p> <code>NONE</code>: The execute command session is not logged.</p> </li> <li> <p> <code>DEFAULT</code>: The <code>awslogs</code> configuration in the task definition is used. If no logging parameter is specified, it defaults to this value. If no <code>awslogs</code> log driver is configured in the task definition, the output won't be logged.</p> </li> <li> <p> <code>OVERRIDE</code>: Specify the logging details as a part of <code>logConfiguration</code>. If the <code>OVERRIDE</code> logging option is specified, the <code>logConfiguration</code> is required.</p> </li> </ul>"""
    log_configuration: NotRequired[
        "aws_sdk_ecs.types.execute_command_log_configuration.ExecuteCommandLogConfiguration"
    ]
    """<p>The log configuration for the results of the execute command actions. The logs can be sent to CloudWatch Logs or an Amazon S3 bucket. When <code>logging=OVERRIDE</code> is specified, a <code>logConfiguration</code> must be provided.</p>"""
