"""Generated from Smithy shape ``com.amazonaws.omics#ActivateReadSetSourceItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.job_status_message
    import aws_sdk_omics.types.read_set_activation_job_item_status
    import aws_sdk_omics.types.read_set_id


class ActivateReadSetSourceItem(TypedDict):
    read_set_id: "aws_sdk_omics.types.read_set_id.ReadSetId"
    """<p>The source's read set ID.</p>"""
    status: "aws_sdk_omics.types.read_set_activation_job_item_status.ReadSetActivationJobItemStatus"
    """<p>The source's status.</p>"""
    status_message: NotRequired[
        "aws_sdk_omics.types.job_status_message.JobStatusMessage"
    ]
    """<p>The source's status message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActivateReadSetSourceItem) -> dict:
    out: dict = {}
    out["readSetId"] = value["read_set_id"]
    out["status"] = value["status"]
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> ActivateReadSetSourceItem:
    out: ActivateReadSetSourceItem = {}  # type: ignore[typeddict-item]
    if "readSetId" in data:
        out["read_set_id"] = data["readSetId"]
    else:
        raise DeserializationError("ActivateReadSetSourceItem.read_set_id required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ActivateReadSetSourceItem.status required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    return out
