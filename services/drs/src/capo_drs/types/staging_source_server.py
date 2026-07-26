"""Generated from Smithy shape ``com.amazonaws.drs#StagingSourceServer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.bounded_string
    import capo_drs.types.source_server_arn
    import capo_drs.types.tags_map


class StagingSourceServer(TypedDict, closed=True):
    hostname: NotRequired["capo_drs.types.bounded_string.BoundedString"]
    """<p>Hostname of staging source server.</p>"""
    arn: NotRequired["capo_drs.types.source_server_arn.SourceServerARN"]
    """<p>The ARN of the source server.</p>"""
    tags: NotRequired["capo_drs.types.tags_map.TagsMap"]
    """<p>A list of tags associated with the staging source server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StagingSourceServer) -> dict:
    out: dict = {}
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StagingSourceServer:
    out: StagingSourceServer = {}  # type: ignore[typeddict-item]
    if "hostname" in data:
        out["hostname"] = data["hostname"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "tags" in data:
        import capo_drs.types.tags_map

        out["tags"] = capo_drs.types.tags_map.deserialize_json(data["tags"])
    return out
