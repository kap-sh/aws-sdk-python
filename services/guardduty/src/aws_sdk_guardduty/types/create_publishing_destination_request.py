"""Generated from Smithy shape ``com.amazonaws.guardduty#CreatePublishingDestinationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.client_token
    import aws_sdk_guardduty.types.destination_properties
    import aws_sdk_guardduty.types.destination_type
    import aws_sdk_guardduty.types.detector_id
    import aws_sdk_guardduty.types.tag_map


class CreatePublishingDestinationRequest(TypedDict, closed=True):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    r"""<p>The ID of the GuardDuty detector associated with the publishing destination.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""
    destination_type: NotRequired[
        "aws_sdk_guardduty.types.destination_type.DestinationType"
    ]
    """<p>The type of resource for the publishing destination. Currently only Amazon S3 buckets are supported.</p>"""
    destination_properties: NotRequired[
        "aws_sdk_guardduty.types.destination_properties.DestinationProperties"
    ]
    """<p>The properties of the publishing destination, including the ARNs for the destination and the KMS key used for encryption.</p>"""
    client_token: NotRequired["aws_sdk_guardduty.types.client_token.ClientToken"]
    """<p>The idempotency token for the request.</p>"""
    tags: NotRequired["aws_sdk_guardduty.types.tag_map.TagMap"]
    """<p>The tags to be added to a new publishing destination resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePublishingDestinationRequest) -> dict:
    out: dict = {}
    if "destination_type" in value:
        import aws_sdk_guardduty.types.destination_type

        out["destinationType"] = (
            aws_sdk_guardduty.types.destination_type.serialize_json(
                value["destination_type"]
            )
        )
    if "destination_properties" in value:
        import aws_sdk_guardduty.types.destination_properties

        out["destinationProperties"] = (
            aws_sdk_guardduty.types.destination_properties.serialize_json(
                value["destination_properties"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_guardduty.types.tag_map

        out["tags"] = aws_sdk_guardduty.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreatePublishingDestinationRequest:
    out: CreatePublishingDestinationRequest = {}  # type: ignore[typeddict-item]
    if "destinationType" in data:
        import aws_sdk_guardduty.types.destination_type

        out["destination_type"] = (
            aws_sdk_guardduty.types.destination_type.deserialize_json(
                data["destinationType"]
            )
        )
    if "destinationProperties" in data:
        import aws_sdk_guardduty.types.destination_properties

        out["destination_properties"] = (
            aws_sdk_guardduty.types.destination_properties.deserialize_json(
                data["destinationProperties"]
            )
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_guardduty.types.tag_map

        out["tags"] = aws_sdk_guardduty.types.tag_map.deserialize_json(data["tags"])
    return out
