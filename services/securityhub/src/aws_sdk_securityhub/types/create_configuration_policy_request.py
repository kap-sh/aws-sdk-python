"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateConfigurationPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string
    import aws_sdk_securityhub.types.policy
    import aws_sdk_securityhub.types.tag_map


class CreateConfigurationPolicyRequest(TypedDict):
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The name of the configuration policy. Alphanumeric characters and the following ASCII characters are permitted: <code>-, ., !, *, /</code>. </p>"""
    description: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The description of the configuration policy. </p>"""
    configuration_policy: NotRequired["aws_sdk_securityhub.types.policy.Policy"]
    """<p> An object that defines how Security Hub CSPM is configured. It includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If you provide a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If you provide a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls). </p>"""
    tags: NotRequired["aws_sdk_securityhub.types.tag_map.TagMap"]
    r"""<p> User-defined tags associated with a configuration policy. For more information, see <a href=\"https://docs.aws.amazon.com/securityhub/latest/userguide/tagging-resources.html\">Tagging Security Hub CSPM resources</a> in the <i>Security Hub CSPM user guide</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationPolicyRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "configuration_policy" in value:
        import aws_sdk_securityhub.types.policy

        out["ConfigurationPolicy"] = aws_sdk_securityhub.types.policy.serialize_json(
            value["configuration_policy"]
        )
    if "tags" in value:
        import aws_sdk_securityhub.types.tag_map

        out["Tags"] = aws_sdk_securityhub.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateConfigurationPolicyRequest:
    out: CreateConfigurationPolicyRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ConfigurationPolicy" in data:
        import aws_sdk_securityhub.types.policy

        out["configuration_policy"] = aws_sdk_securityhub.types.policy.deserialize_json(
            data["ConfigurationPolicy"]
        )
    if "Tags" in data:
        import aws_sdk_securityhub.types.tag_map

        out["tags"] = aws_sdk_securityhub.types.tag_map.deserialize_json(data["Tags"])
    return out
