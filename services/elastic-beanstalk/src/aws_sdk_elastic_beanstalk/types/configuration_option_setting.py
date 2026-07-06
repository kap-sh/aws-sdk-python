"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ConfigurationOptionSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_beanstalk.types.configuration_option_name
    import aws_sdk_elastic_beanstalk.types.configuration_option_value
    import aws_sdk_elastic_beanstalk.types.option_namespace
    import aws_sdk_elastic_beanstalk.types.resource_name


class ConfigurationOptionSetting(TypedDict, closed=True):
    resource_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.resource_name.ResourceName"
    ]
    """<p>A unique resource name for the option setting. Use it for a time–based scaling configuration option.</p>"""
    namespace: NotRequired[
        "aws_sdk_elastic_beanstalk.types.option_namespace.OptionNamespace"
    ]
    """<p>A unique namespace that identifies the option's associated AWS resource.</p>"""
    option_name: NotRequired[
        "aws_sdk_elastic_beanstalk.types.configuration_option_name.ConfigurationOptionName"
    ]
    """<p>The name of the configuration option.</p>"""
    value: NotRequired[
        "aws_sdk_elastic_beanstalk.types.configuration_option_value.ConfigurationOptionValue"
    ]
    """<p>The current value for the configuration option.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfigurationOptionSetting, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "resource_name" in value:
        pairs.append((f"{prefix}.ResourceName", str(value["resource_name"])))
    if "namespace" in value:
        pairs.append((f"{prefix}.Namespace", str(value["namespace"])))
    if "option_name" in value:
        pairs.append((f"{prefix}.OptionName", str(value["option_name"])))
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))


def deserialize_query(el: Element) -> ConfigurationOptionSetting:
    out: ConfigurationOptionSetting = {}  # type: ignore[typeddict-item]
    child_resource_name = el.find("ResourceName")
    if child_resource_name is not None:
        out["resource_name"] = str(child_resource_name.text or "")
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    child_option_name = el.find("OptionName")
    if child_option_name is not None:
        out["option_name"] = str(child_option_name.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
