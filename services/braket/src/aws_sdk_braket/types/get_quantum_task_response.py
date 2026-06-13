"""Generated from Smithy shape ``com.amazonaws.braket#GetQuantumTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_braket.types.action_metadata
    import aws_sdk_braket.types.associations
    import aws_sdk_braket.types.device_arn
    import aws_sdk_braket.types.experimental_capabilities
    import aws_sdk_braket.types.job_arn
    import aws_sdk_braket.types.json_value
    import aws_sdk_braket.types.quantum_task_arn
    import aws_sdk_braket.types.quantum_task_queue_info
    import aws_sdk_braket.types.quantum_task_status
    import aws_sdk_braket.types.tags_map


class GetQuantumTaskResponse(TypedDict):
    quantum_task_arn: "aws_sdk_braket.types.quantum_task_arn.QuantumTaskArn"
    """<p>The ARN of the quantum task.</p>"""
    status: "aws_sdk_braket.types.quantum_task_status.QuantumTaskStatus"
    """<p>The status of the quantum task.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason that a quantum task failed.</p>"""
    device_arn: "aws_sdk_braket.types.device_arn.DeviceArn"
    """<p>The ARN of the device the quantum task was run on.</p>"""
    device_parameters: "aws_sdk_braket.types.json_value.JsonValue"
    """<p>The parameters for the device on which the quantum task ran.</p>"""
    shots: "int"
    """<p>The number of shots used in the quantum task.</p>"""
    output_s3_bucket: "str"
    """<p>The S3 bucket where quantum task results are stored.</p>"""
    output_s3_directory: "str"
    """<p>The folder in the S3 bucket where quantum task results are stored.</p>"""
    created_at: "datetime.datetime"
    """<p>The time at which the quantum task was created.</p>"""
    ended_at: NotRequired["datetime.datetime"]
    """<p>The time at which the quantum task ended.</p>"""
    tags: NotRequired["aws_sdk_braket.types.tags_map.TagsMap"]
    """<p>The tags that belong to this quantum task.</p>"""
    job_arn: NotRequired["aws_sdk_braket.types.job_arn.JobArn"]
    """<p>The ARN of the Amazon Braket job associated with the quantum task.</p>"""
    queue_info: NotRequired[
        "aws_sdk_braket.types.quantum_task_queue_info.QuantumTaskQueueInfo"
    ]
    """<p>Queue information for the requested quantum task. Only returned if <code>QueueInfo</code> is specified in the <code>additionalAttributeNames\"</code> field in the <code>GetQuantumTask</code> API request.</p>"""
    associations: NotRequired["aws_sdk_braket.types.associations.Associations"]
    """<p>The list of Amazon Braket resources associated with the quantum task.</p>"""
    num_successful_shots: NotRequired["int"]
    """<p>The number of successful shots for the quantum task. This is available after a successfully completed quantum task.</p>"""
    action_metadata: NotRequired["aws_sdk_braket.types.action_metadata.ActionMetadata"]
    """<p>Metadata about the action performed by the quantum task, including information about the type of action and program counts.</p>"""
    experimental_capabilities: NotRequired[
        "aws_sdk_braket.types.experimental_capabilities.ExperimentalCapabilities"
    ]
    """<p>Enabled experimental capabilities for the quantum task, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQuantumTaskResponse) -> dict:
    out: dict = {}
    out["quantumTaskArn"] = value["quantum_task_arn"]
    out["status"] = value["status"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    out["deviceArn"] = value["device_arn"]
    out["deviceParameters"] = value["device_parameters"]
    out["shots"] = value["shots"]
    out["outputS3Bucket"] = value["output_s3_bucket"]
    out["outputS3Directory"] = value["output_s3_directory"]
    import aws_sdk_braket.types._prelude.timestamp

    out["createdAt"] = aws_sdk_braket.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    if "ended_at" in value:
        import aws_sdk_braket.types._prelude.timestamp

        out["endedAt"] = aws_sdk_braket.types._prelude.timestamp.serialize_json(
            value["ended_at"]
        )
    if "tags" in value:
        import aws_sdk_braket.types.tags_map

        out["tags"] = aws_sdk_braket.types.tags_map.serialize_json(value["tags"])
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    if "queue_info" in value:
        import aws_sdk_braket.types.quantum_task_queue_info

        out["queueInfo"] = aws_sdk_braket.types.quantum_task_queue_info.serialize_json(
            value["queue_info"]
        )
    if "associations" in value:
        import aws_sdk_braket.types.associations

        out["associations"] = aws_sdk_braket.types.associations.serialize_json(
            value["associations"]
        )
    if "num_successful_shots" in value:
        out["numSuccessfulShots"] = value["num_successful_shots"]
    if "action_metadata" in value:
        import aws_sdk_braket.types.action_metadata

        out["actionMetadata"] = aws_sdk_braket.types.action_metadata.serialize_json(
            value["action_metadata"]
        )
    if "experimental_capabilities" in value:
        import aws_sdk_braket.types.experimental_capabilities

        out["experimentalCapabilities"] = (
            aws_sdk_braket.types.experimental_capabilities.serialize_json(
                value["experimental_capabilities"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetQuantumTaskResponse:
    out: GetQuantumTaskResponse = {}  # type: ignore[typeddict-item]
    if "quantumTaskArn" in data:
        out["quantum_task_arn"] = data["quantumTaskArn"]
    else:
        raise DeserializationError("GetQuantumTaskResponse.quantum_task_arn required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetQuantumTaskResponse.status required")
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "deviceArn" in data:
        out["device_arn"] = data["deviceArn"]
    else:
        raise DeserializationError("GetQuantumTaskResponse.device_arn required")
    if "deviceParameters" in data:
        out["device_parameters"] = data["deviceParameters"]
    else:
        raise DeserializationError("GetQuantumTaskResponse.device_parameters required")
    if "shots" in data:
        out["shots"] = data["shots"]
    else:
        raise DeserializationError("GetQuantumTaskResponse.shots required")
    if "outputS3Bucket" in data:
        out["output_s3_bucket"] = data["outputS3Bucket"]
    else:
        raise DeserializationError("GetQuantumTaskResponse.output_s3_bucket required")
    if "outputS3Directory" in data:
        out["output_s3_directory"] = data["outputS3Directory"]
    else:
        raise DeserializationError(
            "GetQuantumTaskResponse.output_s3_directory required"
        )
    if "createdAt" in data:
        import aws_sdk_braket.types._prelude.timestamp

        out["created_at"] = aws_sdk_braket.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("GetQuantumTaskResponse.created_at required")
    if "endedAt" in data:
        import aws_sdk_braket.types._prelude.timestamp

        out["ended_at"] = aws_sdk_braket.types._prelude.timestamp.deserialize_json(
            data["endedAt"]
        )
    if "tags" in data:
        import aws_sdk_braket.types.tags_map

        out["tags"] = aws_sdk_braket.types.tags_map.deserialize_json(data["tags"])
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    if "queueInfo" in data:
        import aws_sdk_braket.types.quantum_task_queue_info

        out["queue_info"] = (
            aws_sdk_braket.types.quantum_task_queue_info.deserialize_json(
                data["queueInfo"]
            )
        )
    if "associations" in data:
        import aws_sdk_braket.types.associations

        out["associations"] = aws_sdk_braket.types.associations.deserialize_json(
            data["associations"]
        )
    if "numSuccessfulShots" in data:
        out["num_successful_shots"] = data["numSuccessfulShots"]
    if "actionMetadata" in data:
        import aws_sdk_braket.types.action_metadata

        out["action_metadata"] = aws_sdk_braket.types.action_metadata.deserialize_json(
            data["actionMetadata"]
        )
    if "experimentalCapabilities" in data:
        import aws_sdk_braket.types.experimental_capabilities

        out["experimental_capabilities"] = (
            aws_sdk_braket.types.experimental_capabilities.deserialize_json(
                data["experimentalCapabilities"]
            )
        )
    return out
