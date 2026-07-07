"""Generated from Smithy shape ``com.amazonaws.chime#PhoneNumberAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.iso8601_timestamp
    import aws_sdk_chime.types.phone_number_association_name
    import aws_sdk_chime.types.string


class PhoneNumberAssociation(TypedDict, closed=True):
    value: NotRequired["aws_sdk_chime.types.string.String"]
    """<p>Contains the ID for the entity specified in Name.</p>"""
    name: NotRequired[
        "aws_sdk_chime.types.phone_number_association_name.PhoneNumberAssociationName"
    ]
    """<p>Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.</p>"""
    associated_timestamp: NotRequired[
        "aws_sdk_chime.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The timestamp of the phone number association, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberAssociation) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "name" in value:
        import aws_sdk_chime.types.phone_number_association_name

        out["Name"] = aws_sdk_chime.types.phone_number_association_name.serialize_json(
            value["name"]
        )
    if "associated_timestamp" in value:
        import aws_sdk_chime.types.iso8601_timestamp

        out["AssociatedTimestamp"] = (
            aws_sdk_chime.types.iso8601_timestamp.serialize_json(
                value["associated_timestamp"]
            )
        )
    return out


def deserialize_json(data: dict) -> PhoneNumberAssociation:
    out: PhoneNumberAssociation = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Name" in data:
        import aws_sdk_chime.types.phone_number_association_name

        out["name"] = (
            aws_sdk_chime.types.phone_number_association_name.deserialize_json(
                data["Name"]
            )
        )
    if "AssociatedTimestamp" in data:
        import aws_sdk_chime.types.iso8601_timestamp

        out["associated_timestamp"] = (
            aws_sdk_chime.types.iso8601_timestamp.deserialize_json(
                data["AssociatedTimestamp"]
            )
        )
    return out
