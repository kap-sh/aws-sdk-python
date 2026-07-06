"""Generated from Smithy shape ``com.amazonaws.socialmessaging#WabaSetupFinalization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.tag_list
    import aws_sdk_socialmessaging.types.whats_app_business_account_event_destinations
    import aws_sdk_socialmessaging.types.whats_app_business_account_id


class WabaSetupFinalization(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_socialmessaging.types.whats_app_business_account_id.WhatsAppBusinessAccountId"
    ]
    """<p>The ID of the linked WhatsApp Business Account, formatted as <code>waba-01234567890123456789012345678901</code>.</p>"""
    event_destinations: NotRequired[
        "aws_sdk_socialmessaging.types.whats_app_business_account_event_destinations.WhatsAppBusinessAccountEventDestinations"
    ]
    """<p>The event destinations for the linked WhatsApp Business Account.</p>"""
    tags: NotRequired["aws_sdk_socialmessaging.types.tag_list.TagList"]
    """<p>An array of key and value pair tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WabaSetupFinalization) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "event_destinations" in value:
        import aws_sdk_socialmessaging.types.whats_app_business_account_event_destinations

        out["eventDestinations"] = (
            aws_sdk_socialmessaging.types.whats_app_business_account_event_destinations.serialize_json(
                value["event_destinations"]
            )
        )
    if "tags" in value:
        import aws_sdk_socialmessaging.types.tag_list

        out["tags"] = aws_sdk_socialmessaging.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> WabaSetupFinalization:
    out: WabaSetupFinalization = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "eventDestinations" in data:
        import aws_sdk_socialmessaging.types.whats_app_business_account_event_destinations

        out["event_destinations"] = (
            aws_sdk_socialmessaging.types.whats_app_business_account_event_destinations.deserialize_json(
                data["eventDestinations"]
            )
        )
    if "tags" in data:
        import aws_sdk_socialmessaging.types.tag_list

        out["tags"] = aws_sdk_socialmessaging.types.tag_list.deserialize_json(
            data["tags"]
        )
    return out
