"""Generated from Smithy shape ``com.amazonaws.efs#DescribeTagsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_efs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_efs.types.marker
    import aws_sdk_efs.types.tags


class DescribeTagsResponse(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_efs.types.marker.Marker"]
    """<p>If the request included a <code>Marker</code>, the response returns that value in this field.</p>"""
    tags: "aws_sdk_efs.types.tags.Tags"
    """<p>Returns tags associated with the file system as an array of <code>Tag</code> objects. </p>"""
    next_marker: NotRequired["aws_sdk_efs.types.marker.Marker"]
    """<p>If a value is present, there are more tags to return. In a subsequent request, you can provide the value of <code>NextMarker</code> as the value of the <code>Marker</code> parameter in your next request to retrieve the next set of tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeTagsResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    import aws_sdk_efs.types.tags

    out["Tags"] = aws_sdk_efs.types.tags.serialize_json(value["tags"])
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> DescribeTagsResponse:
    out: DescribeTagsResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "Tags" in data:
        import aws_sdk_efs.types.tags

        out["tags"] = aws_sdk_efs.types.tags.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("DescribeTagsResponse.tags required")
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    return out
