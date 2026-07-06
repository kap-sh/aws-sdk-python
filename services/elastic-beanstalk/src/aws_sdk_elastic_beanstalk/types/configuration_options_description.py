"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ConfigurationOptionsDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.configuration_option_descriptions_list
    import aws_sdk_elastic_beanstalk.types.platform_arn
    import aws_sdk_elastic_beanstalk.types.solution_stack_name


class ConfigurationOptionsDescription(TypedDict, closed=True):
    solution_stack_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.solution_stack_name.SolutionStackName"
    ]
    """<p>The name of the solution stack these configuration options belong to.</p>"""
    platform_arn: NotRequired[
        "aws_sdk_elastic_beanstalk.types.platform_arn.PlatformArn"
    ]
    """<p>The ARN of the platform version.</p>"""
    options: NotRequired[
        "aws_sdk_elastic_beanstalk.types.configuration_option_descriptions_list.ConfigurationOptionDescriptionsList"
    ]
    """<p> A list of <a>ConfigurationOptionDescription</a>. </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfigurationOptionsDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "solution_stack_name" in value:
        pairs.append((f"{prefix}.SolutionStackName", str(value["solution_stack_name"])))
    if "platform_arn" in value:
        pairs.append((f"{prefix}.PlatformArn", str(value["platform_arn"])))
    if "options" in value:
        import aws_sdk_elastic_beanstalk.types.configuration_option_descriptions_list

        aws_sdk_elastic_beanstalk.types.configuration_option_descriptions_list.serialize_query(
            value["options"], pairs, f"{prefix}.Options"
        )


def deserialize_query(el: Element) -> ConfigurationOptionsDescription:
    out: ConfigurationOptionsDescription = {}  # type: ignore[typeddict-item]
    child_solution_stack_name = el.find("SolutionStackName")
    if child_solution_stack_name is not None:
        out["solution_stack_name"] = str(child_solution_stack_name.text or "")
    child_platform_arn = el.find("PlatformArn")
    if child_platform_arn is not None:
        out["platform_arn"] = str(child_platform_arn.text or "")
    child_options = el.find("Options")
    if child_options is not None:
        import aws_sdk_elastic_beanstalk.types.configuration_option_descriptions_list

        out["options"] = (
            aws_sdk_elastic_beanstalk.types.configuration_option_descriptions_list.deserialize_query(
                child_options
            )
        )
    return out
