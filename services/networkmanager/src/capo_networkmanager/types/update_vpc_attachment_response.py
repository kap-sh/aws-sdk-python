"""Generated from Smithy shape ``com.amazonaws.networkmanager#UpdateVpcAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.vpc_attachment


class UpdateVpcAttachmentResponse(TypedDict, closed=True):
    vpc_attachment: NotRequired[
        "capo_networkmanager.types.vpc_attachment.VpcAttachment"
    ]
    """<p>Describes the updated VPC attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateVpcAttachmentResponse) -> dict:
    out: dict = {}
    if "vpc_attachment" in value:
        import capo_networkmanager.types.vpc_attachment

        out["VpcAttachment"] = capo_networkmanager.types.vpc_attachment.serialize_json(
            value["vpc_attachment"]
        )
    return out


def deserialize_json(data: dict) -> UpdateVpcAttachmentResponse:
    out: UpdateVpcAttachmentResponse = {}  # type: ignore[typeddict-item]
    if "VpcAttachment" in data:
        import capo_networkmanager.types.vpc_attachment

        out["vpc_attachment"] = (
            capo_networkmanager.types.vpc_attachment.deserialize_json(
                data["VpcAttachment"]
            )
        )
    return out
