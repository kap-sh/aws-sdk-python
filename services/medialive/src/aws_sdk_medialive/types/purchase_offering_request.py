"""Generated from Smithy shape ``com.amazonaws.medialive#PurchaseOfferingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min1
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.renewal_settings
    import aws_sdk_medialive.types.tags


class PurchaseOfferingRequest(TypedDict):
    count: NotRequired["aws_sdk_medialive.types.__integer_min1.__integerMin1"]
    """Number of resources"""
    name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Name for the new reservation"""
    offering_id: "aws_sdk_medialive.types.__string.__string"
    """Offering to purchase, e.g. '87654321'"""
    renewal_settings: NotRequired[
        "aws_sdk_medialive.types.renewal_settings.RenewalSettings"
    ]
    """Renewal settings for the reservation"""
    request_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Unique request ID to be specified. This is needed to prevent retries from creating multiple resources."""
    start: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """Requested reservation start time (UTC) in ISO-8601 format. The specified time must be between the first day of the current month and one year from now. If no value is given, the default is now."""
    tags: NotRequired["aws_sdk_medialive.types.tags.Tags"]
    """A collection of key-value pairs"""


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseOfferingRequest) -> dict:
    out: dict = {}
    if "count" in value:
        out["count"] = value["count"]
    if "name" in value:
        out["name"] = value["name"]
    if "renewal_settings" in value:
        import aws_sdk_medialive.types.renewal_settings

        out["renewalSettings"] = (
            aws_sdk_medialive.types.renewal_settings.serialize_json(
                value["renewal_settings"]
            )
        )
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "start" in value:
        out["start"] = value["start"]
    if "tags" in value:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> PurchaseOfferingRequest:
    out: PurchaseOfferingRequest = {}  # type: ignore[typeddict-item]
    if "count" in data:
        out["count"] = data["count"]
    if "name" in data:
        out["name"] = data["name"]
    if "renewalSettings" in data:
        import aws_sdk_medialive.types.renewal_settings

        out["renewal_settings"] = (
            aws_sdk_medialive.types.renewal_settings.deserialize_json(
                data["renewalSettings"]
            )
        )
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "start" in data:
        out["start"] = data["start"]
    if "tags" in data:
        import aws_sdk_medialive.types.tags

        out["tags"] = aws_sdk_medialive.types.tags.deserialize_json(data["tags"])
    return out
