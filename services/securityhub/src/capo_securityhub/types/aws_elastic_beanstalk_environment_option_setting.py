"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElasticBeanstalkEnvironmentOptionSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsElasticBeanstalkEnvironmentOptionSetting(TypedDict, closed=True):
    namespace: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of resource that the configuration option is associated with.</p>"""
    option_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the option.</p>"""
    resource_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the resource.</p>"""
    value: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The value of the configuration setting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsElasticBeanstalkEnvironmentOptionSetting) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["Namespace"] = value["namespace"]
    if "option_name" in value:
        out["OptionName"] = value["option_name"]
    if "resource_name" in value:
        out["ResourceName"] = value["resource_name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> AwsElasticBeanstalkEnvironmentOptionSetting:
    out: AwsElasticBeanstalkEnvironmentOptionSetting = {}  # type: ignore[typeddict-item]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    if "OptionName" in data:
        out["option_name"] = data["OptionName"]
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
