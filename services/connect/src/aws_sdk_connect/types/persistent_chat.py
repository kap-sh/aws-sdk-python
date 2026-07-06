"""Generated from Smithy shape ``com.amazonaws.connect#PersistentChat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.rehydration_type


class PersistentChat(TypedDict, closed=True):
    rehydration_type: NotRequired[
        "aws_sdk_connect.types.rehydration_type.RehydrationType"
    ]
    """<p>The contactId that is used for rehydration depends on the rehydration type. RehydrationType is required for persistent chat. </p> <ul> <li> <p> <code>ENTIRE_PAST_SESSION</code>: Rehydrates a chat from the most recently terminated past chat contact of the specified past ended chat session. To use this type, provide the <code>initialContactId</code> of the past ended chat session in the <code>sourceContactId</code> field. In this type, Connect Customer determines the most recent chat contact on the specified chat session that has ended, and uses it to start a persistent chat. </p> </li> <li> <p> <code>FROM_SEGMENT</code>: Rehydrates a chat from the past chat contact that is specified in the <code>sourceContactId</code> field. </p> </li> </ul> <p>The actual contactId used for rehydration is provided in the response of this API. </p>"""
    source_contact_id: NotRequired["aws_sdk_connect.types.contact_id.ContactId"]
    """<p>The contactId from which a persistent chat session must be started.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PersistentChat) -> dict:
    out: dict = {}
    if "rehydration_type" in value:
        import aws_sdk_connect.types.rehydration_type

        out["RehydrationType"] = aws_sdk_connect.types.rehydration_type.serialize_json(
            value["rehydration_type"]
        )
    if "source_contact_id" in value:
        out["SourceContactId"] = value["source_contact_id"]
    return out


def deserialize_json(data: dict) -> PersistentChat:
    out: PersistentChat = {}  # type: ignore[typeddict-item]
    if "RehydrationType" in data:
        import aws_sdk_connect.types.rehydration_type

        out["rehydration_type"] = (
            aws_sdk_connect.types.rehydration_type.deserialize_json(
                data["RehydrationType"]
            )
        )
    if "SourceContactId" in data:
        out["source_contact_id"] = data["SourceContactId"]
    return out
