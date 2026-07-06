"""Generated from Smithy shape ``com.amazonaws.comprehend#ExtractedCharactersListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.integer


class ExtractedCharactersListItem(TypedDict, closed=True):
    page: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>Page number.</p>"""
    count: NotRequired["aws_sdk_comprehend.types.integer.Integer"]
    """<p>Number of characters extracted from each page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtractedCharactersListItem) -> dict:
    out: dict = {}
    if "page" in value:
        out["Page"] = value["page"]
    if "count" in value:
        out["Count"] = value["count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtractedCharactersListItem:
    out: ExtractedCharactersListItem = {}  # type: ignore[typeddict-item]
    if "Page" in data:
        out["page"] = data["Page"]
    if "Count" in data:
        out["count"] = data["Count"]
    return out
