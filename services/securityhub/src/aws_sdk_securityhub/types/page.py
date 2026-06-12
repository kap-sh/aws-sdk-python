"""Generated from Smithy shape ``com.amazonaws.securityhub#Page``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.long
    import aws_sdk_securityhub.types.range


class Page(TypedDict):
    page_number: NotRequired["aws_sdk_securityhub.types.long.Long"]
    """<p>The page number of the page that contains the sensitive data.</p>"""
    line_range: NotRequired["aws_sdk_securityhub.types.range.Range"]
    """<p>An occurrence of sensitive data detected in a non-binary text file or a Microsoft Word file. Non-binary text files include files such as HTML, XML, JSON, and TXT files.</p>"""
    offset_range: NotRequired["aws_sdk_securityhub.types.range.Range"]
    """<p>An occurrence of sensitive data detected in a binary text file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Page) -> dict:
    out: dict = {}
    if "page_number" in value:
        out["PageNumber"] = value["page_number"]
    if "line_range" in value:
        import aws_sdk_securityhub.types.range

        out["LineRange"] = aws_sdk_securityhub.types.range.serialize_json(
            value["line_range"]
        )
    if "offset_range" in value:
        import aws_sdk_securityhub.types.range

        out["OffsetRange"] = aws_sdk_securityhub.types.range.serialize_json(
            value["offset_range"]
        )
    return out


def deserialize_json(data: dict) -> Page:
    out: Page = {}  # type: ignore[typeddict-item]
    if "PageNumber" in data:
        out["page_number"] = data["PageNumber"]
    if "LineRange" in data:
        import aws_sdk_securityhub.types.range

        out["line_range"] = aws_sdk_securityhub.types.range.deserialize_json(
            data["LineRange"]
        )
    if "OffsetRange" in data:
        import aws_sdk_securityhub.types.range

        out["offset_range"] = aws_sdk_securityhub.types.range.deserialize_json(
            data["OffsetRange"]
        )
    return out
