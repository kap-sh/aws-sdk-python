"""Generated from Smithy shape ``com.amazonaws.networkmanager#VpcAttachment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.attachment
    import aws_sdk_networkmanager.types.subnet_arn_list
    import aws_sdk_networkmanager.types.vpc_options


class VpcAttachment(TypedDict):
    attachment: NotRequired["aws_sdk_networkmanager.types.attachment.Attachment"]
    """<p>Provides details about the VPC attachment.</p>"""
    subnet_arns: NotRequired[
        "aws_sdk_networkmanager.types.subnet_arn_list.SubnetArnList"
    ]
    """<p>The subnet ARNs.</p>"""
    options: NotRequired["aws_sdk_networkmanager.types.vpc_options.VpcOptions"]
    """<p>Provides details about the VPC attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcAttachment) -> dict:
    out: dict = {}
    if "attachment" in value:
        import aws_sdk_networkmanager.types.attachment

        out["Attachment"] = aws_sdk_networkmanager.types.attachment.serialize_json(
            value["attachment"]
        )
    if "subnet_arns" in value:
        import aws_sdk_networkmanager.types.subnet_arn_list

        out["SubnetArns"] = aws_sdk_networkmanager.types.subnet_arn_list.serialize_json(
            value["subnet_arns"]
        )
    if "options" in value:
        import aws_sdk_networkmanager.types.vpc_options

        out["Options"] = aws_sdk_networkmanager.types.vpc_options.serialize_json(
            value["options"]
        )
    return out


def deserialize_json(data: dict) -> VpcAttachment:
    out: VpcAttachment = {}  # type: ignore[typeddict-item]
    if "Attachment" in data:
        import aws_sdk_networkmanager.types.attachment

        out["attachment"] = aws_sdk_networkmanager.types.attachment.deserialize_json(
            data["Attachment"]
        )
    if "SubnetArns" in data:
        import aws_sdk_networkmanager.types.subnet_arn_list

        out["subnet_arns"] = (
            aws_sdk_networkmanager.types.subnet_arn_list.deserialize_json(
                data["SubnetArns"]
            )
        )
    if "Options" in data:
        import aws_sdk_networkmanager.types.vpc_options

        out["options"] = aws_sdk_networkmanager.types.vpc_options.deserialize_json(
            data["Options"]
        )
    return out
