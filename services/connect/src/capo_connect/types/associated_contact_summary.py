"""Generated from Smithy shape ``com.amazonaws.connect#AssociatedContactSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.channel
    import capo_connect.types.contact_id
    import capo_connect.types.contact_initiation_method
    import capo_connect.types.timestamp


class AssociatedContactSummary(TypedDict, closed=True):
    contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The identifier of the contact in this instance of Connect Customer. </p>"""
    contact_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the contact</p>"""
    initiation_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The date and time this contact was initiated, in UTC time.</p>"""
    disconnect_timestamp: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The date and time that the customer endpoint disconnected from the current contact, in UTC time. In transfer scenarios, the DisconnectTimestamp of the previous contact indicates the date and time when that contact ended.</p>"""
    initial_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>If this contact is related to other contacts, this is the ID of the initial contact.</p>"""
    previous_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>If this contact is not the first contact, this is the ID of the previous contact.</p>"""
    related_contact_id: NotRequired["capo_connect.types.contact_id.ContactId"]
    """<p>The contactId that is related to this contact.</p>"""
    initiation_method: NotRequired[
        "capo_connect.types.contact_initiation_method.ContactInitiationMethod"
    ]
    """<p>Indicates how the contact was initiated.</p>"""
    channel: NotRequired["capo_connect.types.channel.Channel"]
    """<p>How the contact reached your contact center.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedContactSummary) -> dict:
    out: dict = {}
    if "contact_id" in value:
        out["ContactId"] = value["contact_id"]
    if "contact_arn" in value:
        out["ContactArn"] = value["contact_arn"]
    if "initiation_timestamp" in value:
        import capo_connect.types.timestamp

        out["InitiationTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["initiation_timestamp"]
        )
    if "disconnect_timestamp" in value:
        import capo_connect.types.timestamp

        out["DisconnectTimestamp"] = capo_connect.types.timestamp.serialize_json(
            value["disconnect_timestamp"]
        )
    if "initial_contact_id" in value:
        out["InitialContactId"] = value["initial_contact_id"]
    if "previous_contact_id" in value:
        out["PreviousContactId"] = value["previous_contact_id"]
    if "related_contact_id" in value:
        out["RelatedContactId"] = value["related_contact_id"]
    if "initiation_method" in value:
        import capo_connect.types.contact_initiation_method

        out["InitiationMethod"] = (
            capo_connect.types.contact_initiation_method.serialize_json(
                value["initiation_method"]
            )
        )
    if "channel" in value:
        import capo_connect.types.channel

        out["Channel"] = capo_connect.types.channel.serialize_json(value["channel"])
    return out


def deserialize_json(data: dict) -> AssociatedContactSummary:
    out: AssociatedContactSummary = {}  # type: ignore[typeddict-item]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    if "ContactArn" in data:
        out["contact_arn"] = data["ContactArn"]
    if "InitiationTimestamp" in data:
        import capo_connect.types.timestamp

        out["initiation_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["InitiationTimestamp"]
        )
    if "DisconnectTimestamp" in data:
        import capo_connect.types.timestamp

        out["disconnect_timestamp"] = capo_connect.types.timestamp.deserialize_json(
            data["DisconnectTimestamp"]
        )
    if "InitialContactId" in data:
        out["initial_contact_id"] = data["InitialContactId"]
    if "PreviousContactId" in data:
        out["previous_contact_id"] = data["PreviousContactId"]
    if "RelatedContactId" in data:
        out["related_contact_id"] = data["RelatedContactId"]
    if "InitiationMethod" in data:
        import capo_connect.types.contact_initiation_method

        out["initiation_method"] = (
            capo_connect.types.contact_initiation_method.deserialize_json(
                data["InitiationMethod"]
            )
        )
    if "Channel" in data:
        import capo_connect.types.channel

        out["channel"] = capo_connect.types.channel.deserialize_json(data["Channel"])
    return out
