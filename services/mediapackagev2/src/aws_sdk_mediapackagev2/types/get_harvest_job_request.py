"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#GetHarvestJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediapackagev2.types.resource_name


class GetHarvestJobRequest(TypedDict):
    channel_group_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the channel group containing the channel associated with the harvest job.</p>"""
    channel_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the channel associated with the harvest job.</p>"""
    origin_endpoint_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the origin endpoint associated with the harvest job.</p>"""
    harvest_job_name: "aws_sdk_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the harvest job to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetHarvestJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetHarvestJobRequest:
    out: GetHarvestJobRequest = {}  # type: ignore[typeddict-item]
    return out
