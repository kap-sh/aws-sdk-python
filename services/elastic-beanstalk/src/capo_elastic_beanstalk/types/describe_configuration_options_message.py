"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#DescribeConfigurationOptionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.application_name
    import capo_elastic_beanstalk.types.configuration_template_name
    import capo_elastic_beanstalk.types.environment_name
    import capo_elastic_beanstalk.types.options_specifier_list
    import capo_elastic_beanstalk.types.platform_arn
    import capo_elastic_beanstalk.types.solution_stack_name


class DescribeConfigurationOptionsMessage(TypedDict, closed=True):
    application_name: NotRequired[
        "capo_elastic_beanstalk.types.application_name.ApplicationName"
    ]
    """<p>The name of the application associated with the configuration template or environment. Only needed if you want to describe the configuration options associated with either the configuration template or environment.</p>"""
    template_name: NotRequired[
        "capo_elastic_beanstalk.types.configuration_template_name.ConfigurationTemplateName"
    ]
    """<p>The name of the configuration template whose configuration options you want to describe.</p>"""
    environment_name: NotRequired[
        "capo_elastic_beanstalk.types.environment_name.EnvironmentName"
    ]
    """<p>The name of the environment whose configuration options you want to describe.</p>"""
    solution_stack_name: NotRequired[
        "capo_elastic_beanstalk.types.solution_stack_name.SolutionStackName"
    ]
    """<p>The name of the solution stack whose configuration options you want to describe.</p>"""
    platform_arn: NotRequired["capo_elastic_beanstalk.types.platform_arn.PlatformArn"]
    """<p>The ARN of the custom platform.</p>"""
    options: NotRequired[
        "capo_elastic_beanstalk.types.options_specifier_list.OptionsSpecifierList"
    ]
    """<p>If specified, restricts the descriptions to only the specified options.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeConfigurationOptionsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "application_name" in value:
        pairs.append((f"{key_prefix}ApplicationName", str(value["application_name"])))
    if "template_name" in value:
        pairs.append((f"{key_prefix}TemplateName", str(value["template_name"])))
    if "environment_name" in value:
        pairs.append((f"{key_prefix}EnvironmentName", str(value["environment_name"])))
    if "solution_stack_name" in value:
        pairs.append(
            (f"{key_prefix}SolutionStackName", str(value["solution_stack_name"]))
        )
    if "platform_arn" in value:
        pairs.append((f"{key_prefix}PlatformArn", str(value["platform_arn"])))
    if "options" in value:
        import capo_elastic_beanstalk.types.options_specifier_list

        capo_elastic_beanstalk.types.options_specifier_list.serialize_query(
            value["options"], pairs, f"{key_prefix}Options"
        )


def deserialize_query(el: Element) -> DescribeConfigurationOptionsMessage:
    out: DescribeConfigurationOptionsMessage = {}  # type: ignore[typeddict-item]
    child_application_name = el.find("ApplicationName")
    if child_application_name is not None:
        out["application_name"] = str(child_application_name.text or "")
    child_template_name = el.find("TemplateName")
    if child_template_name is not None:
        out["template_name"] = str(child_template_name.text or "")
    child_environment_name = el.find("EnvironmentName")
    if child_environment_name is not None:
        out["environment_name"] = str(child_environment_name.text or "")
    child_solution_stack_name = el.find("SolutionStackName")
    if child_solution_stack_name is not None:
        out["solution_stack_name"] = str(child_solution_stack_name.text or "")
    child_platform_arn = el.find("PlatformArn")
    if child_platform_arn is not None:
        out["platform_arn"] = str(child_platform_arn.text or "")
    child_options = el.find("Options")
    if child_options is not None:
        import capo_elastic_beanstalk.types.options_specifier_list

        out["options"] = (
            capo_elastic_beanstalk.types.options_specifier_list.deserialize_query(
                child_options
            )
        )
    return out
