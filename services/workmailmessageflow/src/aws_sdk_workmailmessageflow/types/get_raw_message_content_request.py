"""Generated from Smithy shape ``com.amazonaws.workmailmessageflow#GetRawMessageContentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_workmailmessageflow.types.message_id_type


class GetRawMessageContentRequest(TypedDict, closed=True):
    message_id: "aws_sdk_workmailmessageflow.types.message_id_type.messageIdType"
    """<p>The identifier of the email message to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRawMessageContentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRawMessageContentRequest:
    out: GetRawMessageContentRequest = {}  # type: ignore[typeddict-item]
    return out
