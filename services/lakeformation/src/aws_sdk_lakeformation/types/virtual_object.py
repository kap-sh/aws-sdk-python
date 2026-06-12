"""Generated from Smithy shape ``com.amazonaws.lakeformation#VirtualObject``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.e_tag_string
    import aws_sdk_lakeformation.types.uri


class VirtualObject(TypedDict):
    uri: "aws_sdk_lakeformation.types.uri.URI"
    """<p>The path to the Amazon S3 object. Must start with s3://</p>"""
    e_tag: NotRequired["aws_sdk_lakeformation.types.e_tag_string.ETagString"]
    """<p>The ETag of the Amazon S3 object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VirtualObject) -> dict:
    out: dict = {}
    out["Uri"] = value["uri"]
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    return out


def deserialize_json(data: dict) -> VirtualObject:
    out: VirtualObject = {}  # type: ignore[typeddict-item]
    if "Uri" in data:
        out["uri"] = data["Uri"]
    else:
        raise DeserializationError("VirtualObject.uri required")
    if "ETag" in data:
        out["e_tag"] = data["ETag"]
    return out
