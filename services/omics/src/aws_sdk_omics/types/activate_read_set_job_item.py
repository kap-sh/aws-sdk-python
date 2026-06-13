"""Generated from Smithy shape ``com.amazonaws.omics#ActivateReadSetJobItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_omics.types.activation_job_id
    import aws_sdk_omics.types.read_set_activation_job_status
    import aws_sdk_omics.types.sequence_store_id


class ActivateReadSetJobItem(TypedDict):
    id: "aws_sdk_omics.types.activation_job_id.ActivationJobId"
    """<p>The job's ID.</p>"""
    sequence_store_id: "aws_sdk_omics.types.sequence_store_id.SequenceStoreId"
    """<p>The job's sequence store ID.</p>"""
    status: (
        "aws_sdk_omics.types.read_set_activation_job_status.ReadSetActivationJobStatus"
    )
    """<p>The job's status.</p>"""
    creation_time: "datetime.datetime"
    """<p>When the job was created.</p>"""
    completion_time: NotRequired["datetime.datetime"]
    """<p>When the job completed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActivateReadSetJobItem) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["sequenceStoreId"] = value["sequence_store_id"]
    out["status"] = value["status"]
    import aws_sdk_omics.types._prelude.timestamp

    out["creationTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "completion_time" in value:
        import aws_sdk_omics.types._prelude.timestamp

        out["completionTime"] = aws_sdk_omics.types._prelude.timestamp.serialize_json(
            value["completion_time"]
        )
    return out


def deserialize_json(data: dict) -> ActivateReadSetJobItem:
    out: ActivateReadSetJobItem = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ActivateReadSetJobItem.id required")
    if "sequenceStoreId" in data:
        out["sequence_store_id"] = data["sequenceStoreId"]
    else:
        raise DeserializationError("ActivateReadSetJobItem.sequence_store_id required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ActivateReadSetJobItem.status required")
    if "creationTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["creation_time"] = aws_sdk_omics.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("ActivateReadSetJobItem.creation_time required")
    if "completionTime" in data:
        import aws_sdk_omics.types._prelude.timestamp

        out["completion_time"] = (
            aws_sdk_omics.types._prelude.timestamp.deserialize_json(
                data["completionTime"]
            )
        )
    return out
