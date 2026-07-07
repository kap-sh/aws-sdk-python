"""Generated from Smithy shape ``com.amazonaws.securityhub#Occurrences``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.cells
    import aws_sdk_securityhub.types.pages
    import aws_sdk_securityhub.types.ranges
    import aws_sdk_securityhub.types.records


class Occurrences(TypedDict, closed=True):
    line_ranges: NotRequired["aws_sdk_securityhub.types.ranges.Ranges"]
    """<p>Occurrences of sensitive data detected in a non-binary text file or a Microsoft Word file. Non-binary text files include files such as HTML, XML, JSON, and TXT files.</p>"""
    offset_ranges: NotRequired["aws_sdk_securityhub.types.ranges.Ranges"]
    """<p>Occurrences of sensitive data detected in a binary text file.</p>"""
    pages: NotRequired["aws_sdk_securityhub.types.pages.Pages"]
    """<p>Occurrences of sensitive data in an Adobe Portable Document Format (PDF) file.</p>"""
    records: NotRequired["aws_sdk_securityhub.types.records.Records"]
    """<p>Occurrences of sensitive data in an Apache Avro object container or an Apache Parquet file.</p>"""
    cells: NotRequired["aws_sdk_securityhub.types.cells.Cells"]
    """<p>Occurrences of sensitive data detected in Microsoft Excel workbooks, comma-separated value (CSV) files, or tab-separated value (TSV) files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Occurrences) -> dict:
    out: dict = {}
    if "line_ranges" in value:
        import aws_sdk_securityhub.types.ranges

        out["LineRanges"] = aws_sdk_securityhub.types.ranges.serialize_json(
            value["line_ranges"]
        )
    if "offset_ranges" in value:
        import aws_sdk_securityhub.types.ranges

        out["OffsetRanges"] = aws_sdk_securityhub.types.ranges.serialize_json(
            value["offset_ranges"]
        )
    if "pages" in value:
        import aws_sdk_securityhub.types.pages

        out["Pages"] = aws_sdk_securityhub.types.pages.serialize_json(value["pages"])
    if "records" in value:
        import aws_sdk_securityhub.types.records

        out["Records"] = aws_sdk_securityhub.types.records.serialize_json(
            value["records"]
        )
    if "cells" in value:
        import aws_sdk_securityhub.types.cells

        out["Cells"] = aws_sdk_securityhub.types.cells.serialize_json(value["cells"])
    return out


def deserialize_json(data: dict) -> Occurrences:
    out: Occurrences = {}  # type: ignore[typeddict-item]
    if "LineRanges" in data:
        import aws_sdk_securityhub.types.ranges

        out["line_ranges"] = aws_sdk_securityhub.types.ranges.deserialize_json(
            data["LineRanges"]
        )
    if "OffsetRanges" in data:
        import aws_sdk_securityhub.types.ranges

        out["offset_ranges"] = aws_sdk_securityhub.types.ranges.deserialize_json(
            data["OffsetRanges"]
        )
    if "Pages" in data:
        import aws_sdk_securityhub.types.pages

        out["pages"] = aws_sdk_securityhub.types.pages.deserialize_json(data["Pages"])
    if "Records" in data:
        import aws_sdk_securityhub.types.records

        out["records"] = aws_sdk_securityhub.types.records.deserialize_json(
            data["Records"]
        )
    if "Cells" in data:
        import aws_sdk_securityhub.types.cells

        out["cells"] = aws_sdk_securityhub.types.cells.deserialize_json(data["Cells"])
    return out
