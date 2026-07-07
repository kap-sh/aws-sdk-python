"""Generated from Smithy shape ``com.amazonaws.mediapackage#CreateHarvestJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackage.types.__string
    import aws_sdk_mediapackage.types.s3_destination


class CreateHarvestJobRequest(TypedDict, closed=True):
    end_time: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """The end of the time-window which will be harvested"""
    id: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """The ID of the HarvestJob. The ID must be unique within the region and it cannot be changed after the HarvestJob is submitted"""
    origin_endpoint_id: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """The ID of the OriginEndpoint that the HarvestJob will harvest from. This cannot be changed after the HarvestJob is submitted."""
    s3_destination: NotRequired[
        "aws_sdk_mediapackage.types.s3_destination.S3Destination"
    ]
    start_time: NotRequired["aws_sdk_mediapackage.types.__string.__string"]
    """The start of the time-window which will be harvested"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateHarvestJobRequest) -> dict:
    out: dict = {}
    if "end_time" in value:
        out["endTime"] = value["end_time"]
    if "id" in value:
        out["id"] = value["id"]
    if "origin_endpoint_id" in value:
        out["originEndpointId"] = value["origin_endpoint_id"]
    if "s3_destination" in value:
        import aws_sdk_mediapackage.types.s3_destination

        out["s3Destination"] = aws_sdk_mediapackage.types.s3_destination.serialize_json(
            value["s3_destination"]
        )
    if "start_time" in value:
        out["startTime"] = value["start_time"]
    return out


def deserialize_json(data: dict) -> CreateHarvestJobRequest:
    out: CreateHarvestJobRequest = {}  # type: ignore[typeddict-item]
    if "endTime" in data:
        out["end_time"] = data["endTime"]
    if "id" in data:
        out["id"] = data["id"]
    if "originEndpointId" in data:
        out["origin_endpoint_id"] = data["originEndpointId"]
    if "s3Destination" in data:
        import aws_sdk_mediapackage.types.s3_destination

        out["s3_destination"] = (
            aws_sdk_mediapackage.types.s3_destination.deserialize_json(
                data["s3Destination"]
            )
        )
    if "startTime" in data:
        out["start_time"] = data["startTime"]
    return out
