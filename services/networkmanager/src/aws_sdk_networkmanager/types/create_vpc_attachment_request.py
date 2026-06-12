"""Generated from Smithy shape ``com.amazonaws.networkmanager#CreateVpcAttachmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_networkmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.client_token
    import aws_sdk_networkmanager.types.constrained_string
    import aws_sdk_networkmanager.types.core_network_id
    import aws_sdk_networkmanager.types.subnet_arn_list
    import aws_sdk_networkmanager.types.tag_list
    import aws_sdk_networkmanager.types.vpc_arn
    import aws_sdk_networkmanager.types.vpc_options


class CreateVpcAttachmentRequest(TypedDict):
    core_network_id: "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of a core network for the VPC attachment.</p>"""
    vpc_arn: "aws_sdk_networkmanager.types.vpc_arn.VpcArn"
    """<p>The ARN of the VPC.</p>"""
    subnet_arns: "aws_sdk_networkmanager.types.subnet_arn_list.SubnetArnList"
    """<p>The subnet ARN of the VPC attachment.</p>"""
    options: NotRequired["aws_sdk_networkmanager.types.vpc_options.VpcOptions"]
    """<p>Options for the VPC attachment.</p>"""
    routing_policy_label: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string.ConstrainedString"
    ]
    """<p>The routing policy label to apply to the VPC attachment for traffic routing decisions.</p>"""
    tags: NotRequired["aws_sdk_networkmanager.types.tag_list.TagList"]
    """<p>The key-value tags associated with the request.</p>"""
    client_token: NotRequired["aws_sdk_networkmanager.types.client_token.ClientToken"]
    """<p>The client token associated with the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateVpcAttachmentRequest) -> dict:
    out: dict = {}
    out["CoreNetworkId"] = value["core_network_id"]
    out["VpcArn"] = value["vpc_arn"]
    import aws_sdk_networkmanager.types.subnet_arn_list

    out["SubnetArns"] = aws_sdk_networkmanager.types.subnet_arn_list.serialize_json(
        value["subnet_arns"]
    )
    if "options" in value:
        import aws_sdk_networkmanager.types.vpc_options

        out["Options"] = aws_sdk_networkmanager.types.vpc_options.serialize_json(
            value["options"]
        )
    if "routing_policy_label" in value:
        out["RoutingPolicyLabel"] = value["routing_policy_label"]
    if "tags" in value:
        import aws_sdk_networkmanager.types.tag_list

        out["Tags"] = aws_sdk_networkmanager.types.tag_list.serialize_json(
            value["tags"]
        )
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
        import aws_sdk_networkmanager.types.subnet_arn_list

        out["subnet_arns"] = (
            aws_sdk_networkmanager.types.subnet_arn_list.deserialize_json(
                data["SubnetArns"]
            )
        )
    else:
        raise DeserializationError("CreateVpcAttachmentRequest.subnet_arns required")
    if "Options" in data:
        import aws_sdk_networkmanager.types.vpc_options

        out["options"] = aws_sdk_networkmanager.types.vpc_options.deserialize_json(
            data["Options"]
        )
    if "RoutingPolicyLabel" in data:
        out["routing_policy_label"] = data["RoutingPolicyLabel"]
    if "Tags" in data:
        import aws_sdk_networkmanager.types.tag_list

        out["tags"] = aws_sdk_networkmanager.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
