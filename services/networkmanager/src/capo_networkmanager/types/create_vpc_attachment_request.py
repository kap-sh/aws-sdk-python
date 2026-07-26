"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateVpcAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_networkmanager.types.client_token
    import capo_networkmanager.types.constrained_string
    import capo_networkmanager.types.core_network_id
    import capo_networkmanager.types.subnet_arn_list
    import capo_networkmanager.types.tag_list
    import capo_networkmanager.types.vpc_arn
    import capo_networkmanager.types.vpc_options


class CreateVpcAttachmentRequest(TypedDict, closed=True):
    core_network_id: "capo_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of a core network for the VPC attachment.</p>"""
    vpc_arn: "capo_networkmanager.types.vpc_arn.VpcArn"
    """<p>The ARN of the VPC.</p>"""
    subnet_arns: "capo_networkmanager.types.subnet_arn_list.SubnetArnList"
    """<p>The subnet ARN of the VPC attachment.</p>"""
    options: NotRequired["capo_networkmanager.types.vpc_options.VpcOptions"]
    """<p>Options for the VPC attachment.</p>"""
    routing_policy_label: NotRequired[
        "capo_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The routing policy label to apply to the VPC attachment for traffic routing decisions.</p>"""
    tags: NotRequired["capo_networkmanager.types.tag_list.TagList"]
    """<p>The key-value tags associated with the request.</p>"""
    client_token: NotRequired["capo_networkmanager.types.client_token.ClientToken"]
    """<p>The client token associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVpcAttachmentRequest) -> dict:
    out: dict = {}
    out["CoreNetworkId"] = value["core_network_id"]
    out["VpcArn"] = value["vpc_arn"]
    import capo_networkmanager.types.subnet_arn_list

    out["SubnetArns"] = capo_networkmanager.types.subnet_arn_list.serialize_json(
        value["subnet_arns"]
    )
    if "options" in value:
        import capo_networkmanager.types.vpc_options

        out["Options"] = capo_networkmanager.types.vpc_options.serialize_json(
            value["options"]
        )
    if "routing_policy_label" in value:
        out["RoutingPolicyLabel"] = value["routing_policy_label"]
    if "tags" in value:
        import capo_networkmanager.types.tag_list

        out["Tags"] = capo_networkmanager.types.tag_list.serialize_json(value["tags"])
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateVpcAttachmentRequest:
    out: CreateVpcAttachmentRequest = {}  # type: ignore[typeddict-item]
    if "CoreNetworkId" in data:
        out["core_network_id"] = data["CoreNetworkId"]
    else:
        raise DeserializationError(
            "CreateVpcAttachmentRequest.core_network_id required"
        )
    if "VpcArn" in data:
        out["vpc_arn"] = data["VpcArn"]
    else:
        raise DeserializationError("CreateVpcAttachmentRequest.vpc_arn required")
    if "SubnetArns" in data:
        import capo_networkmanager.types.subnet_arn_list

        out["subnet_arns"] = capo_networkmanager.types.subnet_arn_list.deserialize_json(
            data["SubnetArns"]
        )
    else:
        raise DeserializationError("CreateVpcAttachmentRequest.subnet_arns required")
    if "Options" in data:
        import capo_networkmanager.types.vpc_options

        out["options"] = capo_networkmanager.types.vpc_options.deserialize_json(
            data["Options"]
        )
    if "RoutingPolicyLabel" in data:
        out["routing_policy_label"] = data["RoutingPolicyLabel"]
    if "Tags" in data:
        import capo_networkmanager.types.tag_list

        out["tags"] = capo_networkmanager.types.tag_list.deserialize_json(data["Tags"])
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
