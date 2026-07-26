"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationMappingUpdateSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.scope_tags_map
    import capo_mgn.types.segment_id


class StartNetworkMigrationMappingUpdateSegment(TypedDict, closed=True):
    segment_id: "capo_mgn.types.segment_id.SegmentID"
    """<p>The ID of the segment to update.</p>"""
    target_account: NotRequired["capo_mgn.types.account_id.AccountID"]
    """<p>The updated target AWS account for the segment.</p>"""
    scope_tags: NotRequired["capo_mgn.types.scope_tags_map.ScopeTagsMap"]
    """<p>The updated scope tags for the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationMappingUpdateSegment) -> dict:
    out: dict = {}
    out["segmentID"] = value["segment_id"]
    if "target_account" in value:
        out["targetAccount"] = value["target_account"]
    if "scope_tags" in value:
        import capo_mgn.types.scope_tags_map

        out["scopeTags"] = capo_mgn.types.scope_tags_map.serialize_json(
            value["scope_tags"]
        )
    return out


def deserialize_json(data: dict) -> StartNetworkMigrationMappingUpdateSegment:
    out: StartNetworkMigrationMappingUpdateSegment = {}  # type: ignore[typeddict-item]
    if "segmentID" in data:
        out["segment_id"] = data["segmentID"]
    else:
        raise DeserializationError(
            "StartNetworkMigrationMappingUpdateSegment.segment_id required"
        )
    if "targetAccount" in data:
        out["target_account"] = data["targetAccount"]
    if "scopeTags" in data:
        import capo_mgn.types.scope_tags_map

        out["scope_tags"] = capo_mgn.types.scope_tags_map.deserialize_json(
            data["scopeTags"]
        )
    return out
