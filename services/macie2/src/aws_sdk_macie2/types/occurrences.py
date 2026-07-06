"""Generated from Smithy shape ``com.amazonaws.macie2#Occurrences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_macie2.types.cells
    import aws_sdk_macie2.types.pages
    import aws_sdk_macie2.types.ranges
    import aws_sdk_macie2.types.records


class Occurrences(TypedDict, closed=True):
    cells: NotRequired["aws_sdk_macie2.types.cells.Cells"]
    """<p>An array of objects, one for each occurrence of sensitive data in a Microsoft Excel workbook, CSV file, or TSV file. This value is null for all other types of files.</p> <p>Each Cell object specifies a cell or field that contains the sensitive data.</p>"""
    line_ranges: NotRequired["aws_sdk_macie2.types.ranges.Ranges"]
    """<p>An array of objects, one for each occurrence of sensitive data in an email message or a non-binary text file such as an HTML, TXT, or XML file. Each Range object specifies a line or inclusive range of lines that contains the sensitive data, and the position of the data on the specified line or lines.</p> <p>This value is often null for file types that are supported by Cell, Page, or Record objects. Exceptions are the location of sensitive data in: unstructured sections of an otherwise structured file, such as a comment in a file; a malformed file that Amazon Macie analyzes as plain text; and, a CSV or TSV file that has any column names that contain sensitive data.</p>"""
    offset_ranges: NotRequired["aws_sdk_macie2.types.ranges.Ranges"]
    """<p>Reserved for future use.</p>"""
    pages: NotRequired["aws_sdk_macie2.types.pages.Pages"]
    """<p>An array of objects, one for each occurrence of sensitive data in an Adobe Portable Document Format file. This value is null for all other types of files.</p> <p>Each Page object specifies a page that contains the sensitive data.</p>"""
    records: NotRequired["aws_sdk_macie2.types.records.Records"]
    """<p>An array of objects, one for each occurrence of sensitive data in an Apache Avro object container, Apache Parquet file, JSON file, or JSON Lines file. This value is null for all other types of files.</p> <p>For an Avro object container or Parquet file, each Record object specifies a record index and the path to a field in a record that contains the sensitive data. For a JSON or JSON Lines file, each Record object specifies the path to a field or array that contains the sensitive data. For a JSON Lines file, it also specifies the index of the line that contains the data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Occurrences) -> dict:
    out: dict = {}
    if "cells" in value:
        import aws_sdk_macie2.types.cells

        out["cells"] = aws_sdk_macie2.types.cells.serialize_json(value["cells"])
    if "line_ranges" in value:
        import aws_sdk_macie2.types.ranges

        out["lineRanges"] = aws_sdk_macie2.types.ranges.serialize_json(
            value["line_ranges"]
        )
    if "offset_ranges" in value:
        import aws_sdk_macie2.types.ranges

        out["offsetRanges"] = aws_sdk_macie2.types.ranges.serialize_json(
            value["offset_ranges"]
        )
    if "pages" in value:
        import aws_sdk_macie2.types.pages

        out["pages"] = aws_sdk_macie2.types.pages.serialize_json(value["pages"])
    if "records" in value:
        import aws_sdk_macie2.types.records

        out["records"] = aws_sdk_macie2.types.records.serialize_json(value["records"])
    return out


def deserialize_json(data: dict) -> Occurrences:
    out: Occurrences = {}  # type: ignore[typeddict-item]
    if "cells" in data:
        import aws_sdk_macie2.types.cells

        out["cells"] = aws_sdk_macie2.types.cells.deserialize_json(data["cells"])
    if "lineRanges" in data:
        import aws_sdk_macie2.types.ranges

        out["line_ranges"] = aws_sdk_macie2.types.ranges.deserialize_json(
            data["lineRanges"]
        )
    if "offsetRanges" in data:
        import aws_sdk_macie2.types.ranges

        out["offset_ranges"] = aws_sdk_macie2.types.ranges.deserialize_json(
            data["offsetRanges"]
        )
    if "pages" in data:
        import aws_sdk_macie2.types.pages

        out["pages"] = aws_sdk_macie2.types.pages.deserialize_json(data["pages"])
    if "records" in data:
        import aws_sdk_macie2.types.records

        out["records"] = aws_sdk_macie2.types.records.deserialize_json(data["records"])
    return out
