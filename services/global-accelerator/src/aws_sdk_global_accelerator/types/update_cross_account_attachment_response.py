"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#UpdateCrossAccountAttachmentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.attachment


class UpdateCrossAccountAttachmentResponse(TypedDict, closed=True):
    cross_account_attachment: NotRequired[
        "aws_sdk_global_accelerator.types.attachment.Attachment"
    ]
    """<p>Information about the updated cross-account attachment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCrossAccountAttachmentResponse) -> dict:
    out: dict = {}
    if "cross_account_attachment" in value:
        import aws_sdk_global_accelerator.types.attachment

        out["CrossAccountAttachment"] = (
            aws_sdk_global_accelerator.types.attachment.serialize_aws_json_1_1(
                value["cross_account_attachment"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCrossAccountAttachmentResponse:
    out: UpdateCrossAccountAttachmentResponse = {}  # type: ignore[typeddict-item]
    if "CrossAccountAttachment" in data:
        import aws_sdk_global_accelerator.types.attachment

        out["cross_account_attachment"] = (
            aws_sdk_global_accelerator.types.attachment.deserialize_aws_json_1_1(
                data["CrossAccountAttachment"]
            )
        )
    return out
