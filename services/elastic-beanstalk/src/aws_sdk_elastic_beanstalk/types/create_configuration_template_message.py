"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#CreateConfigurationTemplateMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.application_name
    import aws_sdk_elastic_beanstalk.types.configuration_option_settings_list
    import aws_sdk_elastic_beanstalk.types.configuration_template_name
    import aws_sdk_elastic_beanstalk.types.description
    import aws_sdk_elastic_beanstalk.types.environment_id
    import aws_sdk_elastic_beanstalk.types.platform_arn
    import aws_sdk_elastic_beanstalk.types.solution_stack_name
    import aws_sdk_elastic_beanstalk.types.source_configuration
    import aws_sdk_elastic_beanstalk.types.tags


class CreateConfigurationTemplateMessage(TypedDict):
    application_name: "aws_sdk_elastic_beanstalk.types.application_name.ApplicationName"
    """<p>The name of the Elastic Beanstalk application to associate with this configuration template.</p>"""
    template_name: "aws_sdk_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
    """<p>The name of the configuration template.</p> <p>Constraint: This name must be unique per application.</p>"""
    solution_stack_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.solution_stack_name.SolutionStackName"
    ]
    r"""<p>The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, <code>64bit Amazon Linux 2013.09 running Tomcat 7 Java 7</code>. A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see <a href=\"https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html\">Supported Platforms</a> in the <i>AWS Elastic Beanstalk Developer Guide</i>.</p> <p>You must specify <code>SolutionStackName</code> if you don't specify <code>PlatformArn</code>, <code>EnvironmentId</code>, or <code>SourceConfiguration</code>.</p> <p>Use the <a href=\"https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ListAvailableSolutionStacks.html\"> <code>ListAvailableSolutionStacks</code> </a> API to obtain a list of available solution stacks.</p>"""
    platform_arn: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_arn.PlatformArn"
    ]
    r"""<p>The Amazon Resource Name (ARN) of the custom platform. For more information, see <a href=\"https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html\"> Custom Platforms</a> in the <i>AWS Elastic Beanstalk Developer Guide</i>.</p> <note> <p>If you specify <code>PlatformArn</code>, then don't specify <code>SolutionStackName</code>.</p> </note>"""
    source_configuration: NotRequired[
        "aws_sdk_elastic_beanstalk.types.source_configuration.SourceConfiguration"
    ]
    """<p>An Elastic Beanstalk configuration template to base this one on. If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.</p> <p>Values specified in <code>OptionSettings</code> override any values obtained from the <code>SourceConfiguration</code>.</p> <p>You must specify <code>SourceConfiguration</code> if you don't specify <code>PlatformArn</code>, <code>EnvironmentId</code>, or <code>SolutionStackName</code>.</p> <p>Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name.</p>"""
    environment_id: NotRequired[
        "aws_sdk_elastic_beanstalk.types.environment_id.EnvironmentId"
    ]
    """<p>The ID of an environment whose settings you want to use to create the configuration template. You must specify <code>EnvironmentId</code> if you don't specify <code>PlatformArn</code>, <code>SolutionStackName</code>, or <code>SourceConfiguration</code>.</p>"""
    description: NotRequired["aws_sdk_elastic_beanstalk.types.description.Description"]
    """<p>An optional description for this configuration.</p>"""
    option_settings: NotRequired[
        "aws_sdk_elastic_beanstalk.types.configuration_option_settings_list.ConfigurationOptionSettingsList"
    ]
    r"""<p>Option values for the Elastic Beanstalk configuration, such as the instance type. If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see <a href=\"https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html\">Option Values</a> in the <i>AWS Elastic Beanstalk Developer Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_elastic_beanstalk.types.tags.Tags"]
    """<p>Specifies the tags applied to the configuration template.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateConfigurationTemplateMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.ApplicationName", str(value["application_name"])))
    pairs.append((f"{prefix}.TemplateName", str(value["template_name"])))
    if "solution_stack_name" in value:
        pairs.append((f"{prefix}.SolutionStackName", str(value["solution_stack_name"])))
    if "platform_arn" in value:
        pairs.append((f"{prefix}.PlatformArn", str(value["platform_arn"])))
    if "source_configuration" in value:
        import aws_sdk_elastic_beanstalk.types.source_configuration

        aws_sdk_elastic_beanstalk.types.source_configuration.serialize_query(
            value["source_configuration"], pairs, f"{prefix}.SourceConfiguration"
        )
    if "environment_id" in value:
        pairs.append((f"{prefix}.EnvironmentId", str(value["environment_id"])))
    if "description" in value:
        pairs.append((f"{prefix}.Description", str(value["description"])))
    if "option_settings" in value:
        import aws_sdk_elastic_beanstalk.types.configuration_option_settings_list

        aws_sdk_elastic_beanstalk.types.configuration_option_settings_list.serialize_query(
            value["option_settings"], pairs, f"{prefix}.OptionSettings"
        )
    if "tags" in value:
        import aws_sdk_elastic_beanstalk.types.tags

        aws_sdk_elastic_beanstalk.types.tags.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CreateConfigurationTemplateMessage:
    out: CreateConfigurationTemplateMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    else:
        raise DeserializationError(
            "CreateConfigurationTemplateMessage.application_name required"
        )
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    else:
        raise DeserializationError(
            "CreateConfigurationTemplateMessage.template_name required"
        )
    child_solution_stack_name = el.find("SolutionStackName")
    if child_solution_stack_name is not None:
        out["solution_stack_name"] = str(child_solution_stack_name.text or "")
    child_platform_arn = el.find("PlatformArn")
    if child_platform_arn is not None:
        out["platform_arn"] = str(child_platform_arn.text or "")
    child_source_configuration = el.find("SourceConfiguration")
    if child_source_configuration is not None:
        import aws_sdk_elastic_beanstalk.types.source_configuration

        out["source_configuration"] = (
            aws_sdk_elastic_beanstalk.types.source_configuration.deserialize_query(
                child_source_configuration
            )
        )
    child_environment_id = el.find("EnvironmentId")
    if child_environment_id is not None:
        out["environment_id"] = str(child_environment_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_option_settings = el.find("OptionSettings")
    if child_option_settings is not None:
        import aws_sdk_elastic_beanstalk.types.configuration_option_settings_list

        out["option_settings"] = (
            aws_sdk_elastic_beanstalk.types.configuration_option_settings_list.deserialize_query(
                child_option_settings
            )
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_elastic_beanstalk.types.tags

        out["tags"] = aws_sdk_elastic_beanstalk.types.tags.deserialize_query(child_tags)
    return out
