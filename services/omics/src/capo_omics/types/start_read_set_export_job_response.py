"""Generated from Smithy shape ``com.amazonaws.omics#StartReadSetExportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.export_job_id
    import capo_omics.types.read_set_export_job_status
    import capo_omics.types.s3_destination
    import capo_omics.types.sequence_store_id


class StartReadSetExportJobResponse(TypedDict, closed=True):
    id: "capo_omics.types.export_job_id.ExportJobId"
    """<p>The job's ID.</p>"""
    sequence_store_id: "capo_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The read set's sequence store ID.</p>"""
    destination: "capo_omics.types.s3_destination.S3Destination"
    """<p>The job's output location.</p>"""
    status: "capo_omics.types.read_set_export_job_status.ReadSetExportJobStatus"
    """<p>The job's status.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the job was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartReadSetExportJobResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["sequenceStoreId"] = value["sequence_store_id"]
    out["destination"] = value["destination"]
    out["status"] = value["status"]
    import capo_omics.types._prelude.timestamp

    out["creationTime"] = capo_omics.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> StartReadSetExportJobResponse:
    out: StartReadSetExportJobResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("StartReadSetExportJobResponse.id required")
    if "sequenceStoreId" in data:
        out["sequence_store_id"] = data["sequenceStoreId"]
    else:
        raise DeserializationError(
            "StartReadSetExportJobResponse.sequence_store_id required"
        )
    if "destination" in data:
        out["destination"] = data["destination"]
    else:
        raise DeserializationError("StartReadSetExportJobResponse.destination required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("StartReadSetExportJobResponse.status required")
    if "creationTime" in data:
        import capo_omics.types._prelude.timestamp

        out["creation_time"] = capo_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError(
            "StartReadSetExportJobResponse.creation_time required"
        )
    return out
