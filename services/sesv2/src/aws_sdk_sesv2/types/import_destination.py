"""Generated from Smithy shape ``com.amazonaws.sesv2#ImportDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.contact_list_destination
    import aws_sdk_sesv2.types.suppression_list_destination


class ImportDestination(TypedDict, closed=True):
    suppression_list_destination: NotRequired[
        "aws_sdk_sesv2.types.suppression_list_destination.SuppressionListDestination"
    ]
    """<p>An object that contains the action of the import job towards suppression list.</p>"""
    contact_list_destination: NotRequired[
        "aws_sdk_sesv2.types.contact_list_destination.ContactListDestination"
    ]
    """<p>An object that contains the action of the import job towards a contact list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportDestination) -> dict:
    out: dict = {}
    if "suppression_list_destination" in value:
        import aws_sdk_sesv2.types.suppression_list_destination

        out["SuppressionListDestination"] = (
            aws_sdk_sesv2.types.suppression_list_destination.serialize_json(
                value["suppression_list_destination"]
            )
        )
    if "contact_list_destination" in value:
        import aws_sdk_sesv2.types.contact_list_destination

        out["ContactListDestination"] = (
            aws_sdk_sesv2.types.contact_list_destination.serialize_json(
                value["contact_list_destination"]
            )
        )
    return out


def deserialize_json(data: dict) -> ImportDestination:
    out: ImportDestination = {}  # type: ignore[typeddict-item]
    if "SuppressionListDestination" in data:
        import aws_sdk_sesv2.types.suppression_list_destination

        out["suppression_list_destination"] = (
            aws_sdk_sesv2.types.suppression_list_destination.deserialize_json(
                data["SuppressionListDestination"]
            )
        )
    if "ContactListDestination" in data:
        import aws_sdk_sesv2.types.contact_list_destination

        out["contact_list_destination"] = (
            aws_sdk_sesv2.types.contact_list_destination.deserialize_json(
                data["ContactListDestination"]
            )
        )
    return out
