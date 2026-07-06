"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_secret_options_list
    import aws_sdk_securityhub.types.field_map
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails(
    TypedDict, closed=True
):
    log_driver: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The log driver to use for the container.</p> <p>Valid values on Fargate are as follows:</p> <ul> <li> <p> <code>awsfirelens</code> </p> </li> <li> <p> <code>awslogs</code> </p> </li> <li> <p> <code>splunk</code> </p> </li> </ul> <p>Valid values on Amazon EC2 are as follows:</p> <ul> <li> <p> <code>awsfirelens</code> </p> </li> <li> <p> <code>awslogs</code> </p> </li> <li> <p> <code>fluentd</code> </p> </li> <li> <p> <code>gelf</code> </p> </li> <li> <p> <code>journald</code> </p> </li> <li> <p> <code>json-file</code> </p> </li> <li> <p> <code>logentries</code> </p> </li> <li> <p> <code>splunk</code> </p> </li> <li> <p> <code>syslog</code> </p> </li> </ul>"""
    options: NotRequired["aws_sdk_securityhub.types.field_map.FieldMap"]
    """<p>The configuration options to send to the log driver. Requires version 1.19 of the Docker Remote API or greater on your container instance.</p>"""
    secret_options: NotRequired[
        "aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_secret_options_list.AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationSecretOptionsList"
    ]
    """<p>The secrets to pass to the log configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails,
) -> dict:
    out: dict = {}
    if "log_driver" in value:
        out["LogDriver"] = value["log_driver"]
    if "options" in value:
        import aws_sdk_securityhub.types.field_map

        out["Options"] = aws_sdk_securityhub.types.field_map.serialize_json(
            value["options"]
        )
    if "secret_options" in value:
        import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_secret_options_list

        out["SecretOptions"] = (
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_secret_options_list.serialize_json(
                value["secret_options"]
            )
        )
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsLogConfigurationDetails = {}  # type: ignore[typeddict-item]
    if "LogDriver" in data:
        out["log_driver"] = data["LogDriver"]
    if "Options" in data:
        import aws_sdk_securityhub.types.field_map

        out["options"] = aws_sdk_securityhub.types.field_map.deserialize_json(
            data["Options"]
        )
    if "SecretOptions" in data:
        import aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_secret_options_list

        out["secret_options"] = (
            aws_sdk_securityhub.types.aws_ecs_task_definition_container_definitions_log_configuration_secret_options_list.deserialize_json(
                data["SecretOptions"]
            )
        )
    return out
