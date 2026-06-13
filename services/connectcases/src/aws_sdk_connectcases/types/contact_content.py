"""Generated from Smithy shape ``com.amazonaws.connectcases#ContactContent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.channel
    import aws_sdk_connectcases.types.connected_to_system_time
    import aws_sdk_connectcases.types.contact_arn


class ContactContent(TypedDict):
    contact_arn: "aws_sdk_connectcases.types.contact_arn.ContactArn"
    """<p>A unique identifier of a contact in Amazon Connect.</p>"""
    channel: "aws_sdk_connectcases.types.channel.Channel"
    """<p>A list of channels to filter on for related items of type <code>Contact</code>.</p>"""
    connected_to_system_time: (
        "aws_sdk_connectcases.types.connected_to_system_time.ConnectedToSystemTime"
    )
    """<p>The difference between the <code>InitiationTimestamp</code> and the <code>DisconnectTimestamp</code> of the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactContent) -> dict:
    out: dict = {}
    out["contactArn"] = value["contact_arn"]
    out["channel"] = value["channel"]
    import aws_sdk_connectcases.types.connected_to_system_time

    out["connectedToSystemTime"] = (
        aws_sdk_connectcases.types.connected_to_system_time.serialize_json(
            value["connected_to_system_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> ContactContent:
    out: ContactContent = {}  # type: ignore[typeddict-item]
    if "contactArn" in data:
        out["contact_arn"] = data["contactArn"]
    else:
        raise DeserializationError("ContactContent.contact_arn required")
    if "channel" in data:
        out["channel"] = data["channel"]
    else:
        raise DeserializationError("ContactContent.channel required")
    if "connectedToSystemTime" in data:
        import aws_sdk_connectcases.types.connected_to_system_time

        out["connected_to_system_time"] = (
            aws_sdk_connectcases.types.connected_to_system_time.deserialize_json(
                data["connectedToSystemTime"]
            )
        )
    else:
        raise DeserializationError("ContactContent.connected_to_system_time required")
    return out
