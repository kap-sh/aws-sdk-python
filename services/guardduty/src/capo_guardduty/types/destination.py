"""Generated from Smithy shape ``com.amazonaws.guardduty#Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.destination_type
    import capo_guardduty.types.publishing_status
    import capo_guardduty.types.string


class Destination(TypedDict, closed=True):
    destination_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The unique ID of the publishing destination.</p>"""
    destination_type: NotRequired[
        "capo_guardduty.types.destination_type.DestinationType"
    ]
    """<p>The type of resource used for the publishing destination. Currently, only Amazon S3 buckets are supported.</p>"""
    status: NotRequired["capo_guardduty.types.publishing_status.PublishingStatus"]
    """<p>The status of the publishing destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> dict:
    out: dict = {}
    if "destination_id" in value:
        out["destinationId"] = value["destination_id"]
    if "destination_type" in value:
        import capo_guardduty.types.destination_type

        out["destinationType"] = capo_guardduty.types.destination_type.serialize_json(
            value["destination_type"]
        )
    if "status" in value:
        import capo_guardduty.types.publishing_status

        out["status"] = capo_guardduty.types.publishing_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    if "destinationId" in data:
        out["destination_id"] = data["destinationId"]
    if "destinationType" in data:
        import capo_guardduty.types.destination_type

        out["destination_type"] = (
            capo_guardduty.types.destination_type.deserialize_json(
                data["destinationType"]
            )
        )
    if "status" in data:
        import capo_guardduty.types.publishing_status

        out["status"] = capo_guardduty.types.publishing_status.deserialize_json(
            data["status"]
        )
    return out
