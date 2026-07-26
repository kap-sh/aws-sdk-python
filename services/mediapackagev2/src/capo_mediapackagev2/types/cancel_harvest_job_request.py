"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CancelHarvestJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediapackagev2.types.entity_tag
    import capo_mediapackagev2.types.resource_name


class CancelHarvestJobRequest(TypedDict, closed=True):
    channel_group_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the channel group containing the channel from which the harvest job is running.</p>"""
    channel_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the channel from which the harvest job is running.</p>"""
    origin_endpoint_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the origin endpoint that the harvest job is harvesting from. This cannot be changed after the harvest job is submitted.</p>"""
    harvest_job_name: "capo_mediapackagev2.types.resource_name.ResourceName"
    """<p>The name of the harvest job to cancel. This name must be unique within the channel and cannot be changed after the harvest job is submitted.</p>"""
    e_tag: NotRequired["capo_mediapackagev2.types.entity_tag.EntityTag"]
    """<p>The current Entity Tag (ETag) associated with the harvest job. Used for concurrency control.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelHarvestJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelHarvestJobRequest:
    out: CancelHarvestJobRequest = {}  # type: ignore[typeddict-item]
    return out
