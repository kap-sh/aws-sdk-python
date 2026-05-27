"""Generated from Smithy shape ``com.amazonaws.ecs#FirelensConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.firelens_configuration_options_map
    import aws_sdk_ecs.types.firelens_configuration_type


class FirelensConfiguration(TypedDict):
    type: "aws_sdk_ecs.types.firelens_configuration_type.FirelensConfigurationType"
    """<p>The log router to use. The valid values are <code>fluentd</code> or <code>fluentbit</code>.</p>"""
    options: NotRequired[
        "aws_sdk_ecs.types.firelens_configuration_options_map.FirelensConfigurationOptionsMap"
    ]
    """<p>The options to use when configuring the log router. This field is optional and can be used to specify a custom configuration file or to add additional metadata, such as the task, task definition, cluster, and container instance details to the log event. If specified, the syntax to use is <code>\"options\":{\"enable-ecs-log-metadata\":\"true|false\",\"config-file-type:\"s3|file\",\"config-file-value\":\"arn:aws:s3:::mybucket/fluent.conf|filepath\"}</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html#firelens-taskdef\">Creating a task definition that uses a FireLens configuration</a> in the <i>Amazon Elastic Container Service Developer Guide</i>.</p> <note> <p>Tasks hosted on Fargate only support the <code>file</code> configuration file type.</p> </note>"""
