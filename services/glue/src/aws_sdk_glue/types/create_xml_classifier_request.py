"""Generated from Smithy shape ``com.amazonaws.glue#CreateXMLClassifierRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.classification
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.row_tag


class CreateXMLClassifierRequest(TypedDict, closed=True):
    classification: "aws_sdk_glue.types.classification.Classification"
    """<p>An identifier of the data format that the classifier matches.</p>"""
    name: "aws_sdk_glue.types.name_string.NameString"
    """<p>The name of the classifier.</p>"""
    row_tag: NotRequired["aws_sdk_glue.types.row_tag.RowTag"]
    r"""<p>The XML tag designating the element that contains each record in an XML document being parsed. This can't identify a self-closing element (closed by <code>/></code>). An empty row element that contains only attributes can be parsed as long as it ends with a closing tag (for example, <code><row item_a=\"A\" item_b=\"B\"></row></code> is okay, but <code><row item_a=\"A\" item_b=\"B\" /></code> is not).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateXMLClassifierRequest) -> dict:
    out: dict = {}
    out["Classification"] = value["classification"]
    out["Name"] = value["name"]
    if "row_tag" in value:
        out["RowTag"] = value["row_tag"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateXMLClassifierRequest:
    out: CreateXMLClassifierRequest = {}  # type: ignore[typeddict-item]
    if "Classification" in data:
        out["classification"] = data["Classification"]
    else:
        raise DeserializationError("CreateXMLClassifierRequest.classification required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateXMLClassifierRequest.name required")
    if "RowTag" in data:
        out["row_tag"] = data["RowTag"]
    return out
