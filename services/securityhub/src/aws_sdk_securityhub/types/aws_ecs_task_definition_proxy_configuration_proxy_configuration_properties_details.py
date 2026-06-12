"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetails(
    TypedDict
):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the property.</p>"""
    value: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The value of the property.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetails,
) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetails:
    out: AwsEcsTaskDefinitionProxyConfigurationProxyConfigurationPropertiesDetails = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
