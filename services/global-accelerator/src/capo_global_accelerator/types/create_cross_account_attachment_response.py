"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CreateCrossAccountAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.attachment


class CreateCrossAccountAttachmentResponse(TypedDict, closed=True):
    cross_account_attachment: NotRequired[
        "capo_global_accelerator.types.attachment.Attachment"
    ]
    """<p>Information about the cross-account attachment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCrossAccountAttachmentResponse) -> dict:
    out: dict = {}
    if "cross_account_attachment" in value:
        import capo_global_accelerator.types.attachment

        out["CrossAccountAttachment"] = (
            capo_global_accelerator.types.attachment.serialize_aws_json_1_1(
                value["cross_account_attachment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCrossAccountAttachmentResponse:
    out: CreateCrossAccountAttachmentResponse = {}  # type: ignore[typeddict-item]
    if "CrossAccountAttachment" in data:
        import capo_global_accelerator.types.attachment

        out["cross_account_attachment"] = (
            capo_global_accelerator.types.attachment.deserialize_aws_json_1_1(
                data["CrossAccountAttachment"]
            )
        )
    return out
