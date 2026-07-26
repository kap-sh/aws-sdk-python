"""Generated from Smithy shape ``com.amazonaws.braket#QuantumTaskSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_braket.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_braket.types.device_arn
    import capo_braket.types.quantum_task_arn
    import capo_braket.types.quantum_task_status
    import capo_braket.types.tags_map


class QuantumTaskSummary(TypedDict, closed=True):
    quantum_task_arn: "capo_braket.types.quantum_task_arn.QuantumTaskArn"
    """<p>The ARN of the quantum task.</p>"""
    status: "capo_braket.types.quantum_task_status.QuantumTaskStatus"
    """<p>The status of the quantum task.</p>"""
    device_arn: "capo_braket.types.device_arn.DeviceArn"
    """<p>The ARN of the device the quantum task ran on.</p>"""
    shots: "int"
    """<p>The shots used for the quantum task.</p>"""
    output_s3_bucket: "str"
    """<p>The S3 bucket where the quantum task result file is stored.</p>"""
    output_s3_directory: "str"
    """<p>The folder in the S3 bucket where the quantum task result file is stored.</p>"""
    created_at: "datetime.datetime"
    """<p>The time at which the quantum task was created.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The time at which the quantum task finished.</p>"""
    tags: NotRequired["capo_braket.types.tags_map.TagsMap"]
    """<p>Displays the key, value pairs of tags associated with this quantum task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuantumTaskSummary) -> dict:
    out: dict = {}
    out["quantumTaskArn"] = value["quantum_task_arn"]
    out["status"] = value["status"]
    out["deviceArn"] = value["device_arn"]
    out["shots"] = value["shots"]
    out["outputS3Bucket"] = value["output_s3_bucket"]
    out["outputS3Directory"] = value["output_s3_directory"]
    import capo_braket.types._prelude.timestamp

    out["createdAt"] = capo_braket.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "ended_at" in value:
        import capo_braket.types._prelude.timestamp

        out["endedAt"] = capo_braket.types._prelude.timestamp.serialize_json(
            value["ended_at"]
        )
    if "tags" in value:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> QuantumTaskSummary:
    out: QuantumTaskSummary = {}  # type: ignore[typeddict-item]
    if "quantumTaskArn" in data:
        out["quantum_task_arn"] = data["quantumTaskArn"]
    else:
        raise DeserializationError("QuantumTaskSummary.quantum_task_arn required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("QuantumTaskSummary.status required")
    if "deviceArn" in data:
        out["device_arn"] = data["deviceArn"]
    else:
        raise DeserializationError("QuantumTaskSummary.device_arn required")
    if "shots" in data:
        out["shots"] = data["shots"]
    else:
        raise DeserializationError("QuantumTaskSummary.shots required")
    if "outputS3Bucket" in data:
        out["output_s3_bucket"] = data["outputS3Bucket"]
    else:
        raise DeserializationError("QuantumTaskSummary.output_s3_bucket required")
    if "outputS3Directory" in data:
        out["output_s3_directory"] = data["outputS3Directory"]
    else:
        raise DeserializationError("QuantumTaskSummary.output_s3_directory required")
    if "createdAt" in data:
        import capo_braket.types._prelude.timestamp

        out["created_at"] = capo_braket.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("QuantumTaskSummary.created_at required")
    if "endedAt" in data:
        import capo_braket.types._prelude.timestamp

        out["ended_at"] = capo_braket.types._prelude.timestamp.deserialize_json(
            data["endedAt"]
        )
    if "tags" in data:
        import capo_braket.types.tags_map

        out["tags"] = capo_braket.types.tags_map.deserialize_json(data["tags"])
    return out
