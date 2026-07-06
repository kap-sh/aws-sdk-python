"""Generated from Smithy shape ``com.amazonaws.connectparticipant#CompleteAttachmentUploadRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectparticipant.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectparticipant.types.attachment_id_list
    import aws_sdk_connectparticipant.types.non_empty_client_token
    import aws_sdk_connectparticipant.types.participant_token


class CompleteAttachmentUploadRequest(TypedDict, closed=True):
    attachment_ids: (
        "aws_sdk_connectparticipant.types.attachment_id_list.AttachmentIdList"
    )
    """<p>A list of unique identifiers for the attachments.</p>"""
    client_token: (
        "aws_sdk_connectparticipant.types.non_empty_client_token.NonEmptyClientToken"
    )
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    connection_token: (
        "aws_sdk_connectparticipant.types.participant_token.ParticipantToken"
    )
    """<p>The authentication token associated with the participant's connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CompleteAttachmentUploadRequest) -> dict:
    out: dict = {}
    import aws_sdk_connectparticipant.types.attachment_id_list

    out["AttachmentIds"] = (
        aws_sdk_connectparticipant.types.attachment_id_list.serialize_json(
            value["attachment_ids"]
        )
    )
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CompleteAttachmentUploadRequest:
    out: CompleteAttachmentUploadRequest = {}  # type: ignore[typeddict-item]
    if "AttachmentIds" in data:
        import aws_sdk_connectparticipant.types.attachment_id_list

        out["attachment_ids"] = (
            aws_sdk_connectparticipant.types.attachment_id_list.deserialize_json(
                data["AttachmentIds"]
            )
        )
    else:
        raise DeserializationError(
            "CompleteAttachmentUploadRequest.attachment_ids required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "CompleteAttachmentUploadRequest.client_token required"
        )
    return out
