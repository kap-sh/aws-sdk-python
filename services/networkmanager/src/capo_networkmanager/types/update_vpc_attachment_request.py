"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateVpcAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.attachment_id
    import capo_networkmanager.types.subnet_arn_list
    import capo_networkmanager.types.vpc_options


class UpdateVpcAttachmentRequest(TypedDict, closed=True):
    attachment_id: "capo_networkmanager.types.attachment_id.AttachmentId"
    """<p>The ID of the attachment.</p>"""
    add_subnet_arns: NotRequired[
        "capo_networkmanager.types.subnet_arn_list.SubnetArnList"
    ]
    """<p>Adds a subnet ARN to the VPC attachment.</p>"""
    remove_subnet_arns: NotRequired[
        "capo_networkmanager.types.subnet_arn_list.SubnetArnList"
    ]
    """<p>Removes a subnet ARN from the attachment.</p>"""
    options: NotRequired["capo_networkmanager.types.vpc_options.VpcOptions"]
    """<p>Additional options for updating the VPC attachment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVpcAttachmentRequest) -> dict:
    out: dict = {}
    if "add_subnet_arns" in value:
        import capo_networkmanager.types.subnet_arn_list

        out["AddSubnetArns"] = capo_networkmanager.types.subnet_arn_list.serialize_json(
            value["add_subnet_arns"]
        )
    if "remove_subnet_arns" in value:
        import capo_networkmanager.types.subnet_arn_list

        out["RemoveSubnetArns"] = (
            capo_networkmanager.types.subnet_arn_list.serialize_json(
                value["remove_subnet_arns"]
            )
        )
    if "options" in value:
        import capo_networkmanager.types.vpc_options

        out["Options"] = capo_networkmanager.types.vpc_options.serialize_json(
            value["options"]
        )
    return out


def deserialize_json(data: dict) -> UpdateVpcAttachmentRequest:
    out: UpdateVpcAttachmentRequest = {}  # type: ignore[typeddict-item]
    if "AddSubnetArns" in data:
        import capo_networkmanager.types.subnet_arn_list

        out["add_subnet_arns"] = (
            capo_networkmanager.types.subnet_arn_list.deserialize_json(
                data["AddSubnetArns"]
            )
        )
    if "RemoveSubnetArns" in data:
        import capo_networkmanager.types.subnet_arn_list

        out["remove_subnet_arns"] = (
            capo_networkmanager.types.subnet_arn_list.deserialize_json(
                data["RemoveSubnetArns"]
            )
        )
    if "Options" in data:
        import capo_networkmanager.types.vpc_options

        out["options"] = capo_networkmanager.types.vpc_options.deserialize_json(
            data["Options"]
        )
    return out
