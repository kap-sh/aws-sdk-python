"""Generated from Smithy shape ``com.amazonaws.mgn#StartNetworkMigrationMappingUpdateSegment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.scope_tags_map
    import aws_sdk_mgn.types.segment_id


class StartNetworkMigrationMappingUpdateSegment(TypedDict, closed=True):
    segment_id: "aws_sdk_mgn.types.segment_id.SegmentID"
    """<p>The ID of the segment to update.</p>"""
    target_account: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>The updated target AWS account for the segment.</p>"""
    scope_tags: NotRequired["aws_sdk_mgn.types.scope_tags_map.ScopeTagsMap"]
    """<p>The updated scope tags for the segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartNetworkMigrationMappingUpdateSegment) -> dict:
    out: dict = {}
    out["segmentID"] = value["segment_id"]
    if "target_account" in value:
        out["targetAccount"] = value["target_account"]
    if "scope_tags" in value:
        import aws_sdk_mgn.types.scope_tags_map

        out["scopeTags"] = aws_sdk_mgn.types.scope_tags_map.serialize_json(
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
        import aws_sdk_mgn.types.scope_tags_map

        out["scope_tags"] = aws_sdk_mgn.types.scope_tags_map.deserialize_json(
            data["scopeTags"]
        )
    return out
