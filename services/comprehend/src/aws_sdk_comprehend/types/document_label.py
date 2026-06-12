"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentLabel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.float
    import aws_sdk_comprehend.types.integer
    import aws_sdk_comprehend.types.string


class DocumentLabel(TypedDict):
    name: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>The name of the label.</p>"""
    score: NotRequired["aws_sdk_comprehend.types.float.Float"]
    """<p>The confidence score that Amazon Comprehend has this label correctly attributed.</p>"""
    page: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>Page number where the label occurs. This field is present in the response only if your request includes the <code>Byte</code> parameter. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentLabel) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "score" in value:
        out["Score"] = value["score"]
    if "page" in value:
        out["Page"] = value["page"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentLabel:
    out: DocumentLabel = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Score" in data:
        out["score"] = data["Score"]
    if "Page" in data:
        out["page"] = data["Page"]
    return out
