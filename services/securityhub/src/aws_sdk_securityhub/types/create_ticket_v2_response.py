"""Generated from Smithy shape ``com.amazonaws.securityhub#CreateTicketV2Response``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class CreateTicketV2Response(TypedDict):
    ticket_id: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ID for the ticketv2.</p>"""
    ticket_src_url: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The url to the created ticket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTicketV2Response) -> dict:
    out: dict = {}
    if "ticket_id" in value:
        out["TicketId"] = value["ticket_id"]
    if "ticket_src_url" in value:
        out["TicketSrcUrl"] = value["ticket_src_url"]
    return out


def deserialize_json(data: dict) -> CreateTicketV2Response:
    out: CreateTicketV2Response = {}  # type: ignore[typeddict-item]
    if "TicketId" in data:
        out["ticket_id"] = data["TicketId"]
    if "TicketSrcUrl" in data:
        out["ticket_src_url"] = data["TicketSrcUrl"]
    return out
