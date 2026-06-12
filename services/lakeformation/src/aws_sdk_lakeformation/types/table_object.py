"""Generated from Smithy shape ``com.amazonaws.lakeformation#TableObject``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.e_tag_string
    import aws_sdk_lakeformation.types.object_size
    import aws_sdk_lakeformation.types.uri


class TableObject(TypedDict):
    uri: NotRequired["aws_sdk_lakeformation.types.uri.URI"]
    """<p>The Amazon S3 location of the object.</p>"""
    e_tag: NotRequired["aws_sdk_lakeformation.types.e_tag_string.ETagString"]
    """<p>The Amazon S3 ETag of the object. Returned by <code>GetTableObjects</code> for validation and used to identify changes to the underlying data.</p>"""
    size: "aws_sdk_lakeformation.types.object_size.ObjectSize"
    """<p>The size of the Amazon S3 object in bytes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableObject) -> dict:
    out: dict = {}
    if "uri" in value:
        out["Uri"] = value["uri"]
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    out["Size"] = value.get("size", 0)
    return out


def deserialize_json(data: dict) -> TableObject:
    out: TableObject = {}  # type: ignore[typeddict-item]
    if "Uri" in data:
        out["uri"] = data["Uri"]
    if "ETag" in data:
        out["e_tag"] = data["ETag"]
    if "Size" in data:
        out["size"] = data["Size"]
    else:
        out["size"] = 0
    return out
