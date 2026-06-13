"""Generated from Smithy shape ``com.amazonaws.drs#StagingSourceServer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_drs.types.bounded_string
    import aws_sdk_drs.types.source_server_arn
    import aws_sdk_drs.types.tags_map


class StagingSourceServer(TypedDict):
    hostname: NotRequired["aws_sdk_drs.types.bounded_string.BoundedString"]
    """<p>Hostname of staging source server.</p>"""
    arn: NotRequired["aws_sdk_drs.types.source_server_arn.SourceServerARN"]
    """<p>The ARN of the source server.</p>"""
    tags: NotRequired["aws_sdk_drs.types.tags_map.TagsMap"]
    """<p>A list of tags associated with the staging source server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StagingSourceServer) -> dict:
    out: dict = {}
    if "hostname" in value:
        out["hostname"] = value["hostname"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import aws_sdk_drs.types.tags_map

        out["tags"] = aws_sdk_drs.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StagingSourceServer:
    out: StagingSourceServer = {}  # type: ignore[typeddict-item]
    if "hostname" in data:
        out["hostname"] = data["hostname"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "tags" in data:
        import aws_sdk_drs.types.tags_map

        out["tags"] = aws_sdk_drs.types.tags_map.deserialize_json(data["tags"])
    return out
