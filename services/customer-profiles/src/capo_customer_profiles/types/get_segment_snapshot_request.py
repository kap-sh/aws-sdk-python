"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetSegmentSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.uuid


class GetSegmentSnapshotRequest(TypedDict, closed=True):
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique identifier of the domain.</p>"""
    segment_definition_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the segment definition.</p>"""
    snapshot_id: "capo_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of the segment snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSegmentSnapshotRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSegmentSnapshotRequest:
    out: GetSegmentSnapshotRequest = {}  # type: ignore[typeddict-item]
    return out
