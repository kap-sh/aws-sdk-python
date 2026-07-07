"""Generated from Smithy shape ``com.amazonaws.guardduty#DescribePublishingDestinationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.destination_properties
    import aws_sdk_guardduty.types.destination_type
    import aws_sdk_guardduty.types.long
    import aws_sdk_guardduty.types.publishing_status
    import aws_sdk_guardduty.types.string
    import aws_sdk_guardduty.types.tag_map


class DescribePublishingDestinationResponse(TypedDict, closed=True):
    destination_id: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The ID of the publishing destination.</p>"""
    destination_type: NotRequired[
        "aws_sdk_guardduty.types.destination_type.DestinationType"
    ]
    """<p>The type of publishing destination. Currently, only Amazon S3 buckets are supported.</p>"""
    status: NotRequired["aws_sdk_guardduty.types.publishing_status.PublishingStatus"]
    """<p>The status of the publishing destination.</p>"""
    publishing_failure_start_timestamp: NotRequired["aws_sdk_guardduty.types.long.Long"]
    """<p>The time, in epoch millisecond format, at which GuardDuty was first unable to publish findings to the destination.</p>"""
    destination_properties: NotRequired[
        "aws_sdk_guardduty.types.destination_properties.DestinationProperties"
    ]
    """<p>A <code>DestinationProperties</code> object that includes the <code>DestinationArn</code> and <code>KmsKeyArn</code> of the publishing destination.</p>"""
    tags: NotRequired["aws_sdk_guardduty.types.tag_map.TagMap"]
    """<p>The tags of the publishing destination resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePublishingDestinationResponse) -> dict:
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
    if "publishing_failure_start_timestamp" in value:
        out["publishingFailureStartTimestamp"] = value[
            "publishing_failure_start_timestamp"
        ]
    if "destination_properties" in value:
        import aws_sdk_guardduty.types.destination_properties

        out["destinationProperties"] = (
            aws_sdk_guardduty.types.destination_properties.serialize_json(
                value["destination_properties"]
            )
        )
    if "tags" in value:
        import aws_sdk_guardduty.types.tag_map

        out["tags"] = aws_sdk_guardduty.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> DescribePublishingDestinationResponse:
    out: DescribePublishingDestinationResponse = {}  # type: ignore[typeddict-item]
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
    if "publishingFailureStartTimestamp" in data:
        out["publishing_failure_start_timestamp"] = data[
            "publishingFailureStartTimestamp"
        ]
    if "destinationProperties" in data:
        import aws_sdk_guardduty.types.destination_properties

        out["destination_properties"] = (
            aws_sdk_guardduty.types.destination_properties.deserialize_json(
                data["destinationProperties"]
            )
        )
    if "tags" in data:
        import aws_sdk_guardduty.types.tag_map

        out["tags"] = aws_sdk_guardduty.types.tag_map.deserialize_json(data["tags"])
    return out
