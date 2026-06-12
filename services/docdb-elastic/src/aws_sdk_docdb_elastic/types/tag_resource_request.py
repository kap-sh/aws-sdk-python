"""Generated from Smithy shape ``com.amazonaws.docdbelastic#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.arn
    import aws_sdk_docdb_elastic.types.tag_map


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_docdb_elastic.types.arn.Arn"
    """<p>The ARN identifier of the elastic cluster resource.</p>"""
    tags: "aws_sdk_docdb_elastic.types.tag_map.TagMap"
    """<p>The tags that are assigned to the elastic cluster resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    import aws_sdk_docdb_elastic.types.tag_map

    out["tags"] = aws_sdk_docdb_elastic.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "tags" in data:
        import aws_sdk_docdb_elastic.types.tag_map

        out["tags"] = aws_sdk_docdb_elastic.types.tag_map.deserialize_json(data["tags"])
    else:
        raise DeserializationError("TagResourceRequest.tags required")
    return out
