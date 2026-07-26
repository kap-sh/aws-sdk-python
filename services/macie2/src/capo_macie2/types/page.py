"""Generated from Smithy shape ``com.amazonaws.macie2#Page``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__long
    import capo_macie2.types.range


class Page(TypedDict, closed=True):
    line_range: NotRequired["capo_macie2.types.range.Range"]
    """<p>Reserved for future use.</p>"""
    offset_range: NotRequired["capo_macie2.types.range.Range"]
    """<p>Reserved for future use.</p>"""
    page_number: NotRequired["capo_macie2.types.__long.__long"]
    """<p>The page number of the page that contains the sensitive data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Page) -> dict:
    out: dict = {}
    if "line_range" in value:
        import capo_macie2.types.range

        out["lineRange"] = capo_macie2.types.range.serialize_json(value["line_range"])
    if "offset_range" in value:
        import capo_macie2.types.range

        out["offsetRange"] = capo_macie2.types.range.serialize_json(
            value["offset_range"]
        )
    if "page_number" in value:
        out["pageNumber"] = value["page_number"]
    return out


def deserialize_json(data: dict) -> Page:
    out: Page = {}  # type: ignore[typeddict-item]
    if "lineRange" in data:
        import capo_macie2.types.range

        out["line_range"] = capo_macie2.types.range.deserialize_json(data["lineRange"])
    if "offsetRange" in data:
        import capo_macie2.types.range

        out["offset_range"] = capo_macie2.types.range.deserialize_json(
            data["offsetRange"]
        )
    if "pageNumber" in data:
        out["page_number"] = data["pageNumber"]
    return out
