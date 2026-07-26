"""Generated from Smithy shape ``com.amazonaws.ssm#AttachmentInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.attachment_name


class AttachmentInformation(TypedDict, closed=True):
    name: NotRequired["capo_ssm.types.attachment_name.AttachmentName"]
    """<p>The name of the attachment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttachmentInformation) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AttachmentInformation:
    out: AttachmentInformation = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
