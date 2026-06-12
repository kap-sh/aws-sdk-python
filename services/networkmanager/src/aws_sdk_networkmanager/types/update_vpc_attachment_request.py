"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateVpcAttachmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment_id
    import aws_sdk_networkmanager.types.subnet_arn_list
    import aws_sdk_networkmanager.types.vpc_options


class UpdateVpcAttachmentRequest(TypedDict):
    attachment_id: "aws_sdk_networkmanager.types.attachment_id.AttachmentId"
    """<p>The ID of the attachment.</p>"""
    add_subnet_arns: NotRequired[
        "aws_sdk_networkmanager.types.subnet_arn_list.SubnetArnList"
    ]
    """<p>Adds a subnet ARN to the VPC attachment.</p>"""
    remove_subnet_arns: NotRequired[
        "aws_sdk_networkmanager.types.subnet_arn_list.SubnetArnList"
    ]
    """<p>Removes a subnet ARN from the attachment.</p>"""
    options: NotRequired["aws_sdk_networkmanager.types.vpc_options.VpcOptions"]
    """<p>Additional options for updating the VPC attachment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVpcAttachmentRequest) -> dict:
    out: dict = {}
    if "add_subnet_arns" in value:
        import aws_sdk_networkmanager.types.subnet_arn_list

        out["AddSubnetArns"] = (
            aws_sdk_networkmanager.types.subnet_arn_list.serialize_json(
                value["add_subnet_arns"]
            )
        )
    if "remove_subnet_arns" in value:
        import aws_sdk_networkmanager.types.subnet_arn_list

        out["RemoveSubnetArns"] = (
            aws_sdk_networkmanager.types.subnet_arn_list.serialize_json(
                value["remove_subnet_arns"]
            )
        )
    if "options" in value:
        import aws_sdk_networkmanager.types.vpc_options

        out["Options"] = aws_sdk_networkmanager.types.vpc_options.serialize_json(
            value["options"]
        )
    return out


def deserialize_json(data: dict) -> UpdateVpcAttachmentRequest:
    out: UpdateVpcAttachmentRequest = {}  # type: ignore[typeddict-item]
    if "AddSubnetArns" in data:
        import aws_sdk_networkmanager.types.subnet_arn_list

        out["add_subnet_arns"] = (
            aws_sdk_networkmanager.types.subnet_arn_list.deserialize_json(
                data["AddSubnetArns"]
            )
        )
    if "RemoveSubnetArns" in data:
        import aws_sdk_networkmanager.types.subnet_arn_list

        out["remove_subnet_arns"] = (
            aws_sdk_networkmanager.types.subnet_arn_list.deserialize_json(
                data["RemoveSubnetArns"]
            )
        )
    if "Options" in data:
        import aws_sdk_networkmanager.types.vpc_options

        out["options"] = aws_sdk_networkmanager.types.vpc_options.deserialize_json(
            data["Options"]
        )
    return out
