"""Generated from Smithy shape ``com.amazonaws.omics#ReadOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_omics.types.comment_char
    import aws_sdk_omics.types.encoding
    import aws_sdk_omics.types.escape_char
    import aws_sdk_omics.types.escape_quotes
    import aws_sdk_omics.types.header
    import aws_sdk_omics.types.line_sep
    import aws_sdk_omics.types.quote
    import aws_sdk_omics.types.quote_all
    import aws_sdk_omics.types.separator


class ReadOptions(TypedDict):
    sep: NotRequired["aws_sdk_omics.types.separator.Separator"]
    """<p>The file's field separator.</p>"""
    encoding: NotRequired["aws_sdk_omics.types.encoding.Encoding"]
    """<p>The file's encoding.</p>"""
    quote: NotRequired["aws_sdk_omics.types.quote.Quote"]
    """<p>The file's quote character.</p>"""
    quote_all: "aws_sdk_omics.types.quote_all.QuoteAll"
    """<p>Whether all values need to be quoted, or just those that contain quotes.</p>"""
    escape: NotRequired["aws_sdk_omics.types.escape_char.EscapeChar"]
    """<p>A character for escaping quotes in the file.</p>"""
    escape_quotes: "aws_sdk_omics.types.escape_quotes.EscapeQuotes"
    """<p>Whether quotes need to be escaped in the file.</p>"""
    comment: NotRequired["aws_sdk_omics.types.comment_char.CommentChar"]
    """<p>The file's comment character.</p>"""
    header: "aws_sdk_omics.types.header.Header"
    """<p>Whether the file has a header row.</p>"""
    line_sep: NotRequired["aws_sdk_omics.types.line_sep.LineSep"]
    """<p>A line separator for the file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadOptions) -> dict:
    out: dict = {}
    if "sep" in value:
        out["sep"] = value["sep"]
    if "encoding" in value:
        out["encoding"] = value["encoding"]
    if "quote" in value:
        out["quote"] = value["quote"]
    out["quoteAll"] = value.get("quote_all", False)
    if "escape" in value:
        out["escape"] = value["escape"]
    out["escapeQuotes"] = value.get("escape_quotes", False)
    if "comment" in value:
        out["comment"] = value["comment"]
    out["header"] = value.get("header", False)
    if "line_sep" in value:
        out["lineSep"] = value["line_sep"]
    return out


def deserialize_json(data: dict) -> ReadOptions:
    out: ReadOptions = {}  # type: ignore[typeddict-item]
    if "sep" in data:
        out["sep"] = data["sep"]
    if "encoding" in data:
        out["encoding"] = data["encoding"]
    if "quote" in data:
        out["quote"] = data["quote"]
    if "quoteAll" in data:
        out["quote_all"] = data["quoteAll"]
    else:
        out["quote_all"] = False
    if "escape" in data:
        out["escape"] = data["escape"]
    if "escapeQuotes" in data:
        out["escape_quotes"] = data["escapeQuotes"]
    else:
        out["escape_quotes"] = False
    if "comment" in data:
        out["comment"] = data["comment"]
    if "header" in data:
        out["header"] = data["header"]
    else:
        out["header"] = False
    if "lineSep" in data:
        out["line_sep"] = data["lineSep"]
    return out
