"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttachmentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.attachment_name
    import capo_qbusiness.types.blob
    import capo_qbusiness.types.copy_from_source


class AttachmentInput(TypedDict, closed=True):
    data: NotRequired["capo_qbusiness.types.blob.Blob"]
    """<p>The contents of the attachment.</p>"""
    name: NotRequired["capo_qbusiness.types.attachment_name.AttachmentName"]
    """<p>The filename of the attachment.</p>"""
    copy_from: NotRequired["capo_qbusiness.types.copy_from_source.CopyFromSource"]
    """<p>A reference to an existing attachment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentInput) -> dict:
    out: dict = {}
    if "data" in value:
        import capo_qbusiness.types.blob

        out["data"] = capo_qbusiness.types.blob.serialize_json(value["data"])
    if "name" in value:
        out["name"] = value["name"]
    if "copy_from" in value:
        import capo_qbusiness.types.copy_from_source

        out["copyFrom"] = capo_qbusiness.types.copy_from_source.serialize_json(
            value["copy_from"]
        )
    return out


def deserialize_json(data: dict) -> AttachmentInput:
    out: AttachmentInput = {}  # type: ignore[typeddict-item]
    if "data" in data:
        import capo_qbusiness.types.blob

        out["data"] = capo_qbusiness.types.blob.deserialize_json(data["data"])
    if "name" in data:
        out["name"] = data["name"]
    if "copyFrom" in data:
        import capo_qbusiness.types.copy_from_source

        out["copy_from"] = capo_qbusiness.types.copy_from_source.deserialize_json(
            data["copyFrom"]
        )
    return out
