"""Generated from Smithy shape ``com.amazonaws.mediapackage#DescribeHarvestJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackage.types.__string
    import capo_mediapackage.types.s3_destination
    import capo_mediapackage.types.status


class DescribeHarvestJobResponse(TypedDict, closed=True):
    arn: NotRequired["capo_mediapackage.types.__string.__string"]
    """The Amazon Resource Name (ARN) assigned to the HarvestJob."""
    channel_id: NotRequired["capo_mediapackage.types.__string.__string"]
    """The ID of the Channel that the HarvestJob will harvest from."""
    created_at: NotRequired["capo_mediapackage.types.__string.__string"]
    """The date and time the HarvestJob was submitted."""
    end_time: NotRequired["capo_mediapackage.types.__string.__string"]
    """The end of the time-window which will be harvested."""
    id: NotRequired["capo_mediapackage.types.__string.__string"]
    """The ID of the HarvestJob. The ID must be unique within the region and it cannot be changed after the HarvestJob is submitted."""
    origin_endpoint_id: NotRequired["capo_mediapackage.types.__string.__string"]
    """The ID of the OriginEndpoint that the HarvestJob will harvest from. This cannot be changed after the HarvestJob is submitted."""
    s3_destination: NotRequired["capo_mediapackage.types.s3_destination.S3Destination"]
    start_time: NotRequired["capo_mediapackage.types.__string.__string"]
    """The start of the time-window which will be harvested."""
    status: NotRequired["capo_mediapackage.types.status.Status"]
    """The current status of the HarvestJob. Consider setting up a CloudWatch Event to listen for HarvestJobs as they succeed or fail. In the event of failure, the CloudWatch Event will include an explanation of why the HarvestJob failed."""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeHarvestJobResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "channel_id" in value:
        out["channelId"] = value["channel_id"]
    if "created_at" in value:
        out["createdAt"] = value["created_at"]
    if "end_time" in value:
        out["endTime"] = value["end_time"]
    if "id" in value:
        out["id"] = value["id"]
    if "origin_endpoint_id" in value:
        out["originEndpointId"] = value["origin_endpoint_id"]
    if "s3_destination" in value:
        import capo_mediapackage.types.s3_destination

        out["s3Destination"] = capo_mediapackage.types.s3_destination.serialize_json(
            value["s3_destination"]
        )
    if "start_time" in value:
        out["startTime"] = value["start_time"]
    if "status" in value:
        import capo_mediapackage.types.status

        out["status"] = capo_mediapackage.types.status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DescribeHarvestJobResponse:
    out: DescribeHarvestJobResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "channelId" in data:
        out["channel_id"] = data["channelId"]
    if "createdAt" in data:
        out["created_at"] = data["createdAt"]
    if "endTime" in data:
        out["end_time"] = data["endTime"]
    if "id" in data:
        out["id"] = data["id"]
    if "originEndpointId" in data:
        out["origin_endpoint_id"] = data["originEndpointId"]
    if "s3Destination" in data:
        import capo_mediapackage.types.s3_destination

        out["s3_destination"] = capo_mediapackage.types.s3_destination.deserialize_json(
            data["s3Destination"]
        )
    if "startTime" in data:
        out["start_time"] = data["startTime"]
    if "status" in data:
        import capo_mediapackage.types.status

        out["status"] = capo_mediapackage.types.status.deserialize_json(data["status"])
    return out
