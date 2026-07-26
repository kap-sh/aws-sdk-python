"""Generated from Smithy shape ``com.amazonaws.omics#ExportReadSetFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.read_set_export_job_status


class ExportReadSetFilter(TypedDict, closed=True):
    status: NotRequired[
        "capo_omics.types.read_set_export_job_status.ReadSetExportJobStatus"
    ]
    """<p>A status to filter on.</p>"""
    created_after: NotRequired["datetime.datetime"]
    """<p>The filter's start date.</p>"""
    created_before: NotRequired["datetime.datetime"]
    """<p>The filter's end date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExportReadSetFilter) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "created_after" in value:
        import capo_omics.types._prelude.timestamp

        out["createdAfter"] = capo_omics.types._prelude.timestamp.serialize_json(
            value["created_after"]
        )
    if "created_before" in value:
        import capo_omics.types._prelude.timestamp

        out["createdBefore"] = capo_omics.types._prelude.timestamp.serialize_json(
            value["created_before"]
        )
    return out


def deserialize_json(data: dict) -> ExportReadSetFilter:
    out: ExportReadSetFilter = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "createdAfter" in data:
        import capo_omics.types._prelude.timestamp

        out["created_after"] = capo_omics.types._prelude.timestamp.deserialize_json(
            data["createdAfter"]
        )
    if "createdBefore" in data:
        import capo_omics.types._prelude.timestamp

        out["created_before"] = capo_omics.types._prelude.timestamp.deserialize_json(
            data["createdBefore"]
        )
    return out
