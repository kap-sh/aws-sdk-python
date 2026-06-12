"""Generated from Smithy shape ``com.amazonaws.guardduty#Destination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.destination_type
    import aws_sdk_guardduty.types.publishing_status
    import aws_sdk_guardduty.types.string


class Destination(TypedDict):
    destination_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The unique ID of the publishing destination.</p>"""
    destination_type: NotRequired[
        "aws_sdk_guardduty.types.destination_type.DestinationType"
    ]
    """<p>The type of resource used for the publishing destination. Currently, only Amazon S3 buckets are supported.</p>"""
    status: NotRequired["aws_sdk_guardduty.types.publishing_status.PublishingStatus"]
    """<p>The status of the publishing destination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> dict:
    out: dict = {}
    if "destination_id" in value:
        out["destinationId"] = value["destination_id"]
    if "destination_type" in value:
        import aws_sdk_guardduty.types.destination_type

        out["destinationType"] = (
            aws_sdk_guardduty.types.destination_type.serialize_json(
                value["destination_type"]
            )
        )
    if "status" in value:
        import aws_sdk_guardduty.types.publishing_status

        out["status"] = aws_sdk_guardduty.types.publishing_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    if "destinationId" in data:
        out["destination_id"] = data["destinationId"]
    if "destinationType" in data:
        import aws_sdk_guardduty.types.destination_type

        out["destination_type"] = (
            aws_sdk_guardduty.types.destination_type.deserialize_json(
                data["destinationType"]
            )
        )
    if "status" in data:
        import aws_sdk_guardduty.types.publishing_status

        out["status"] = aws_sdk_guardduty.types.publishing_status.deserialize_json(
            data["status"]
        )
    return out
