"""Generated from Smithy shape ``com.amazonaws.ecs#SubmitAttachmentStateChangesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class SubmitAttachmentStateChangesResponse(TypedDict, closed=True):
    acknowledgment: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>Acknowledgement of the state change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubmitAttachmentStateChangesResponse) -> dict:
    out: dict = {}
    if "acknowledgment" in value:
        out["acknowledgment"] = value["acknowledgment"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SubmitAttachmentStateChangesResponse:
    out: SubmitAttachmentStateChangesResponse = {}  # type: ignore[typeddict-item]
    if "acknowledgment" in data:
        out["acknowledgment"] = data["acknowledgment"]
    return out
