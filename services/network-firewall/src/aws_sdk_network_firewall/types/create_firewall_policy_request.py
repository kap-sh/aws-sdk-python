"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateFirewallPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.boolean
    import aws_sdk_network_firewall.types.description
    import aws_sdk_network_firewall.types.encryption_configuration
    import aws_sdk_network_firewall.types.firewall_policy
    import aws_sdk_network_firewall.types.resource_name
    import aws_sdk_network_firewall.types.tag_list


class CreateFirewallPolicyRequest(TypedDict):
    firewall_policy_name: "aws_sdk_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the firewall policy. You can't change the name of a firewall policy after you create it.</p>"""
    firewall_policy: "aws_sdk_network_firewall.types.firewall_policy.FirewallPolicy"
    """<p>The rule groups and policy actions to use in the firewall policy.</p>"""
    description: NotRequired["aws_sdk_network_firewall.types.description.Description"]
    """<p>A description of the firewall policy.</p>"""
    tags: NotRequired["aws_sdk_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""
    dry_run: "aws_sdk_network_firewall.types.boolean.Boolean"
    """<p>Indicates whether you want Network Firewall to just check the validity of the request, rather than run the request. </p> <p>If set to <code>TRUE</code>, Network Firewall checks whether the request can run successfully, but doesn't actually make the requested changes. The call returns the value that the request would return if you ran it with dry run set to <code>FALSE</code>, but doesn't make additions or changes to your resources. This option allows you to make sure that you have the required permissions to run the request and that your request parameters are valid. </p> <p>If set to <code>FALSE</code>, Network Firewall makes the requested changes to your resources. </p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_network_firewall.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>A complex type that contains settings for encryption of your firewall policy resources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateFirewallPolicyRequest) -> dict:
    out: dict = {}
    out["FirewallPolicyName"] = value["firewall_policy_name"]
    import aws_sdk_network_firewall.types.firewall_policy

    out["FirewallPolicy"] = (
        aws_sdk_network_firewall.types.firewall_policy.serialize_aws_json_1_0(
            value["firewall_policy"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_network_firewall.types.tag_list

        out["Tags"] = aws_sdk_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    out["DryRun"] = value.get("dry_run", False)
    if "encryption_configuration" in value:
        import aws_sdk_network_firewall.types.encryption_configuration

        out["EncryptionConfiguration"] = (
            aws_sdk_network_firewall.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateFirewallPolicyRequest:
    out: CreateFirewallPolicyRequest = {}  # type: ignore[typeddict-item]
    if "FirewallPolicyName" in data:
        out["firewall_policy_name"] = data["FirewallPolicyName"]
    else:
        raise DeserializationError(
            "CreateFirewallPolicyRequest.firewall_policy_name required"
        )
    if "FirewallPolicy" in data:
        import aws_sdk_network_firewall.types.firewall_policy

        out["firewall_policy"] = (
            aws_sdk_network_firewall.types.firewall_policy.deserialize_aws_json_1_0(
                data["FirewallPolicy"]
            )
        )
    else:
        raise DeserializationError(
            "CreateFirewallPolicyRequest.firewall_policy required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_network_firewall.types.tag_list

        out["tags"] = aws_sdk_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    if "EncryptionConfiguration" in data:
        import aws_sdk_network_firewall.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_network_firewall.types.encryption_configuration.deserialize_aws_json_1_0(
                data["EncryptionConfiguration"]
            )
        )
    return out
