"""Generated from Smithy shape ``com.amazonaws.omics#ImportReferenceFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.reference_import_job_status


class ImportReferenceFilter(TypedDict, closed=True):
    status: NotRequired[
        "aws_sdk_omics.types.reference_import_job_status.ReferenceImportJobStatus"
    ]
    """<p>A status to filter on.</p>"""
    created_after: NotRequired["datetime.datetime"]
    """<p>The filter's start date.</p>"""
    created_before: NotRequired["datetime.datetime"]
    """<p>The filter's end date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportReferenceFilter) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "created_after" in value:
        import aws_sdk_omics.types._prelude.timestamp

        out["createdAfter"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
            value["created_after"]
        )
    if "created_before" in value:
        import aws_sdk_omics.types._prelude.timestamp

        out["createdBefore"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
            value["created_before"]
        )
    return out


def deserialize_json(data: dict) -> ImportReferenceFilter:
    out: ImportReferenceFilter = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "createdAfter" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["created_after"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["createdAfter"]
        )
    if "createdBefore" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["created_before"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["createdBefore"]
        )
    return out
