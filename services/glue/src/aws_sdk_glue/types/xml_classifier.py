"""Generated from Smithy shape ``com.amazonaws.glue#XMLClassifier``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.classification
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.row_tag
    import aws_sdk_glue.types.timestamp
    import aws_sdk_glue.types.version_id


class XMLClassifier(TypedDict):
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the classifier.</p>"""
    classification: "aws_sdk_glue.types.classification.Classification"
    """<p>An identifier of the data format that the classifier matches.</p>"""
    creation_time: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The time that this classifier was registered.</p>"""
    last_updated: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>The time that this classifier was last updated.</p>"""
    version: "aws_sdk_glue.types.version_id.VersionId"
    """<p>The version of this classifier.</p>"""
    row_tag: NotRequired["aws_sdk_glue.types.row_tag.RowTag"]
    """<p>The XML tag designating the element that contains each record in an XML document being parsed. This can't identify a self-closing element (closed by <code>/></code>). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, <code><row item_a=\"A\" item_b=\"B\"></row></code> is okay, but <code><row item_a=\"A\" item_b=\"B\" /></code> is not).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: XMLClassifier) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Classification"] = value["classification"]
    if "creation_time" in value:
        import aws_sdk_glue.types.timestamp

        out["CreationTime"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_updated" in value:
        import aws_sdk_glue.types.timestamp

        out["LastUpdated"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["last_updated"]
        )
    out["Version"] = value.get("version", 0)
    if "row_tag" in value:
        out["RowTag"] = value["row_tag"]
    return out


def deserialize_aws_json_1_1(data: dict) -> XMLClassifier:
    out: XMLClassifier = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("XMLClassifier.name required")
    if "Classification" in data:
        out["classification"] = data["Classification"]
    else:
        raise DeserializationError("XMLClassifier.classification required")
    if "CreationTime" in data:
        import aws_sdk_glue.types.timestamp

        out["creation_time"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastUpdated" in data:
        import aws_sdk_glue.types.timestamp

        out["last_updated"] = aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
            data["LastUpdated"]
        )
    if "Version" in data:
        out["version"] = data["Version"]
    else:
        out["version"] = 0
    if "RowTag" in data:
        out["row_tag"] = data["RowTag"]
    return out
