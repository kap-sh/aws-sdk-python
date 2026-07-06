"""Generated from Smithy shape ``com.amazonaws.networkmanager#ProposedNetworkFunctionGroupChange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.integer
    import aws_sdk_networkmanager.types.tag_list


class ProposedNetworkFunctionGroupChange(TypedDict, closed=True):
    tags: NotRequired["aws_sdk_networkmanager.types.tag_list.TagList"]
    """<p>The list of proposed changes to the key-value tags associated with the network function group.</p>"""
    attachment_policy_rule_number: NotRequired[
        "aws_sdk_networkmanager.types.integer.Integer"
    ]
    """<p>The proposed new attachment policy rule number for the network function group.</p>"""
    network_function_group_name: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The proposed name change for the network function group name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProposedNetworkFunctionGroupChange) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_networkmanager.types.tag_list

        out["Tags"] = aws_sdk_networkmanager.types.tag_list.serialize_json(
            value["tags"]
        )
    if "attachment_policy_rule_number" in value:
        out["AttachmentPolicyRuleNumber"] = value["attachment_policy_rule_number"]
    if "network_function_group_name" in value:
        out["NetworkFunctionGroupName"] = value["network_function_group_name"]
    return out


def deserialize_json(data: dict) -> ProposedNetworkFunctionGroupChange:
    out: ProposedNetworkFunctionGroupChange = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_networkmanager.types.tag_list

        out["tags"] = aws_sdk_networkmanager.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if "AttachmentPolicyRuleNumber" in data:
        out["attachment_policy_rule_number"] = data["AttachmentPolicyRuleNumber"]
    if "NetworkFunctionGroupName" in data:
        out["network_function_group_name"] = data["NetworkFunctionGroupName"]
    return out
