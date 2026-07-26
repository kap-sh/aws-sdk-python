"""Generated from Smithy shape ``com.amazonaws.networkmanager#Attachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_error_list
    import capo_networkmanager.types.attachment_id
    import capo_networkmanager.types.attachment_state
    import capo_networkmanager.types.attachment_type
    import capo_networkmanager.types.aws_account_id
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_arn
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.date_time
    import capo_networkmanager.types.external_region_code
    import capo_networkmanager.types.external_region_code_list
    import capo_networkmanager.types.integer
    import capo_networkmanager.types.network_function_group_name
    import capo_networkmanager.types.proposed_network_function_group_change
    import capo_networkmanager.types.proposed_segment_change
    import capo_networkmanager.types.resource_arn
    import capo_networkmanager.types.tag_list


class Attachment(TypedDict, closed=True):
    core_network_id: NotRequired[
        "capo_networkmanager.types.core_network_id.CoreNetworkId"
    ]
    """<p>The ID of a core network.</p>"""
    core_network_arn: NotRequired[
        "capo_networkmanager.types.core_network_arn.CoreNetworkArn"
    ]
    """<p>The ARN of a core network.</p>"""
    attachment_id: NotRequired["capo_networkmanager.types.attachment_id.AttachmentId"]
    """<p>The ID of the attachment.</p>"""
    owner_account_id: NotRequired[
        "capo_networkmanager.types.aws_account_id.AWSAccountId"
    ]
    """<p>The ID of the attachment account owner.</p>"""
    attachment_type: NotRequired[
        "capo_networkmanager.types.attachment_type.AttachmentType"
    ]
    """<p>The type of attachment.</p>"""
    state: NotRequired["capo_networkmanager.types.attachment_state.AttachmentState"]
    """<p>The state of the attachment.</p>"""
    edge_location: NotRequired[
        "capo_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The Region where the edge is located. This is returned for all attachment types except a Direct Connect gateway attachment, which instead returns <code>EdgeLocations</code>.</p>"""
    edge_locations: NotRequired[
        "capo_networkmanager.types.external_region_code_list.ExternalRegionCodeList"
    ]
    """<p>The edge locations that the Direct Connect gateway is associated with. This is returned only for Direct Connect gateway attachments. All other attachment types retrun <code>EdgeLocation</code>.</p>"""
    resource_arn: NotRequired["capo_networkmanager.types.resource_arn.ResourceArn"]
    """<p>The attachment resource ARN.</p>"""
    attachment_policy_rule_number: NotRequired[
        "capo_networkmanager.types.integer.Integer"
    ]
    """<p>The policy rule number associated with the attachment.</p>"""
    segment_name: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The name of the segment attachment.</p>"""
    network_function_group_name: NotRequired[
        "capo_networkmanager.types.network_function_group_name.NetworkFunctionGroupName"
    ]
    """<p>The name of the network function group.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The tags associated with the attachment.</p>"""
    proposed_segment_change: NotRequired[
        "capo_networkmanager.types.proposed_segment_change.ProposedSegmentChange"
    ]
    """<p>The attachment to move from one segment to another.</p>"""
    proposed_network_function_group_change: NotRequired[
        "capo_networkmanager.types.proposed_network_function_group_change.ProposedNetworkFunctionGroupChange"
    ]
    """<p>Describes a proposed change to a network function group associated with the attachment.</p>"""
    created_at: NotRequired["capo_networkmanager.types.date_time.DateTime"]
    """<p>The timestamp when the attachment was created.</p>"""
    updated_at: NotRequired["capo_networkmanager.types.date_time.DateTime"]
    """<p>The timestamp when the attachment was last updated.</p>"""
    last_modification_errors: NotRequired[
        "capo_networkmanager.types.attachment_error_list.AttachmentErrorList"
    ]
    """<p>Describes the error associated with the attachment request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Attachment) -> dict:
    out: dict = {}
    if "core_network_id" in value:
        out["CoreNetworkId"] = value["core_network_id"]
    if "core_network_arn" in value:
        out["CoreNetworkArn"] = value["core_network_arn"]
    if "attachment_id" in value:
        out["AttachmentId"] = value["attachment_id"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "attachment_type" in value:
        import capo_networkmanager.types.attachment_type

        out["AttachmentType"] = (
            capo_networkmanager.types.attachment_type.serialize_json(
                value["attachment_type"]
            )
        )
    if "state" in value:
        import capo_networkmanager.types.attachment_state

        out["State"] = capo_networkmanager.types.attachment_state.serialize_json(
            value["state"]
        )
    if "edge_location" in value:
        out["EdgeLocation"] = value["edge_location"]
    if "edge_locations" in value:
        import capo_networkmanager.types.external_region_code_list

        out["EdgeLocations"] = (
            capo_networkmanager.types.external_region_code_list.serialize_json(
                value["edge_locations"]
            )
        )
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "attachment_policy_rule_number" in value:
        out["AttachmentPolicyRuleNumber"] = value["attachment_policy_rule_number"]
    if "segment_name" in value:
        out["SegmentName"] = value["segment_name"]
    if "network_function_group_name" in value:
        out["NetworkFunctionGroupName"] = value["network_function_group_name"]
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    if "proposed_segment_change" in value:
        import capo_networkmanager.types.proposed_segment_change

        out["ProposedSegmentChange"] = (
            capo_networkmanager.types.proposed_segment_change.serialize_json(
                value["proposed_segment_change"]
            )
        )
    if "proposed_network_function_group_change" in value:
        import capo_networkmanager.types.proposed_network_function_group_change

        out["ProposedNetworkFunctionGroupChange"] = (
            capo_networkmanager.types.proposed_network_function_group_change.serialize_json(
                value["proposed_network_function_group_change"]
            )
        )
    if "created_at" in value:
        import capo_networkmanager.types.date_time

        out["CreatedAt"] = capo_networkmanager.types.date_time.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_networkmanager.types.date_time

        out["UpdatedAt"] = capo_networkmanager.types.date_time.serialize_json(
            value["updated_at"]
        )
    if "last_modification_errors" in value:
        import capo_networkmanager.types.attachment_error_list

        out["LastModificationErrors"] = (
            capo_networkmanager.types.attachment_error_list.serialize_json(
                value["last_modification_errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> Attachment:
    out: Attachment = {}  # type: ignore[typeddict-item]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    if "CoreNetworkArn" in data:
        out["core_network_arn"] = data["CoreNetworkArn"]
    if "AttachmentId" in data:
        out["attachment_id"] = data["AttachmentId"]
    if "OwnerAccountId" in data:
        out["owner_account_id"] = data["OwnerAccountId"]
    if "AttachmentType" in data:
        import capo_networkmanager.types.attachment_type

        out["attachment_type"] = (
            capo_networkmanager.types.attachment_type.deserialize_json(
                data["AttachmentType"]
            )
        )
    if "State" in data:
        import capo_networkmanager.types.attachment_state

        out["state"] = capo_networkmanager.types.attachment_state.deserialize_json(
            data["State"]
        )
    if "EdgeLocation" in data:
        out["edge_location"] = data["EdgeLocation"]
    if "EdgeLocations" in data:
        import capo_networkmanager.types.external_region_code_list

        out["edge_locations"] = (
            capo_networkmanager.types.external_region_code_list.deserialize_json(
                data["EdgeLocations"]
            )
        )
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "AttachmentPolicyRuleNumber" in data:
        out["attachment_policy_rule_number"] = data["AttachmentPolicyRuleNumber"]
    if "SegmentName" in data:
        out["segment_name"] = data["SegmentName"]
    if "NetworkFunctionGroupName" in data:
        out["network_function_group_name"] = data["NetworkFunctionGroupName"]
    if "Tags" in data:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    if "ProposedSegmentChange" in data:
        import capo_networkmanager.types.proposed_segment_change

        out["proposed_segment_change"] = (
            capo_networkmanager.types.proposed_segment_change.deserialize_json(
                data["ProposedSegmentChange"]
            )
        )
    if "ProposedNetworkFunctionGroupChange" in data:
        import capo_networkmanager.types.proposed_network_function_group_change

        out["proposed_network_function_group_change"] = (
            capo_networkmanager.types.proposed_network_function_group_change.deserialize_json(
                data["ProposedNetworkFunctionGroupChange"]
            )
        )
    if "CreatedAt" in data:
        import capo_networkmanager.types.date_time

        out["created_at"] = capo_networkmanager.types.date_time.deserialize_json(
            data["CreatedAt"]
        )
    if "UpdatedAt" in data:
        import capo_networkmanager.types.date_time

        out["updated_at"] = capo_networkmanager.types.date_time.deserialize_json(
            data["UpdatedAt"]
        )
    if "LastModificationErrors" in data:
        import capo_networkmanager.types.attachment_error_list

        out["last_modification_errors"] = (
            capo_networkmanager.types.attachment_error_list.deserialize_json(
                data["LastModificationErrors"]
            )
        )
    return out
