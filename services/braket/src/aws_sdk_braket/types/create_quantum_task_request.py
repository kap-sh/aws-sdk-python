"""Generated from Smithy shape ``com.amazonaws.braket#CreateQuantumTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_braket.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_braket.types.associations
    import aws_sdk_braket.types.device_arn
    import aws_sdk_braket.types.experimental_capabilities
    import aws_sdk_braket.types.job_token
    import aws_sdk_braket.types.json_value
    import aws_sdk_braket.types.string64
    import aws_sdk_braket.types.tags_map

class CreateQuantumTaskRequest(TypedDict):
    client_token: "aws_sdk_braket.types.string64.String64"
    """<p>The client token associated with the request.</p>"""
    device_arn: "aws_sdk_braket.types.device_arn.DeviceArn"
    """<p>The ARN of the device to run the quantum task on.</p>"""
    device_parameters: NotRequired["aws_sdk_braket.types.json_value.JsonValue"]
    """<p>The parameters for the device to run the quantum task on.</p>"""
    shots: "int"
    """<p>The number of shots to use for the quantum task.</p>"""
    output_s3_bucket: "str"
    """<p>The S3 bucket to store quantum task result files in.</p>"""
    output_s3_key_prefix: "str"
    """<p>The key prefix for the location in the S3 bucket to store quantum task results in.</p>"""
    action: "aws_sdk_braket.types.json_value.JsonValue"
    """<p>The action associated with the quantum task.</p>"""
    tags: NotRequired["aws_sdk_braket.types.tags_map.TagsMap"]
    """<p>Tags to be added to the quantum task you're creating.</p>"""
    job_token: NotRequired["aws_sdk_braket.types.job_token.JobToken"]
    """<p>The token for an Amazon Braket hybrid job that associates it with the quantum task.</p>"""
    associations: NotRequired["aws_sdk_braket.types.associations.Associations"]
    """<p>The list of Amazon Braket resources associated with the quantum task.</p>"""
    experimental_capabilities: NotRequired["aws_sdk_braket.types.experimental_capabilities.ExperimentalCapabilities"]
    """<p>Enable experimental capabilities for the quantum task.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateQuantumTaskRequest) -> dict:
    out: dict = {}
    out["clientToken"] = value["client_token"]
    out["deviceArn"] = value["device_arn"]
    if "device_parameters" in value:
        out["deviceParameters"] = value["device_parameters"]
    out["shots"] = value["shots"]
    out["outputS3Bucket"] = value["output_s3_bucket"]
    out["outputS3KeyPrefix"] = value["output_s3_key_prefix"]
    out["action"] = value["action"]
    if "tags" in value:
        import aws_sdk_braket.types.tags_map
        out["tags"] = aws_sdk_braket.types.tags_map.serialize_json(value["tags"])
    if "job_token" in value:
        out["jobToken"] = value["job_token"]
    if "associations" in value:
        import aws_sdk_braket.types.associations
        out["associations"] = aws_sdk_braket.types.associations.serialize_json(value["associations"])
    if "experimental_capabilities" in value:
        import aws_sdk_braket.types.experimental_capabilities
        out["experimentalCapabilities"] = aws_sdk_braket.types.experimental_capabilities.serialize_json(value["experimental_capabilities"])
    return out


def deserialize_json(data: dict) -> CreateQuantumTaskRequest:
    out: CreateQuantumTaskRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError("CreateQuantumTaskRequest.client_token required")
    if "deviceArn" in data:
        out["device_arn"] = data["deviceArn"]
    else:
        raise DeserializationError("CreateQuantumTaskRequest.device_arn required")
    if "deviceParameters" in data:
        out["device_parameters"] = data["deviceParameters"]
    if "shots" in data:
        out["shots"] = data["shots"]
    else:
        raise DeserializationError("CreateQuantumTaskRequest.shots required")
    if "outputS3Bucket" in data:
        out["output_s3_bucket"] = data["outputS3Bucket"]
    else:
        raise DeserializationError("CreateQuantumTaskRequest.output_s3_bucket required")
    if "outputS3KeyPrefix" in data:
        out["output_s3_key_prefix"] = data["outputS3KeyPrefix"]
    else:
        raise DeserializationError("CreateQuantumTaskRequest.output_s3_key_prefix required")
    if "action" in data:
        out["action"] = data["action"]
    else:
        raise DeserializationError("CreateQuantumTaskRequest.action required")
    if "tags" in data:
        import aws_sdk_braket.types.tags_map
        out["tags"] = aws_sdk_braket.types.tags_map.deserialize_json(data["tags"])
    if "jobToken" in data:
        out["job_token"] = data["jobToken"]
    if "associations" in data:
        import aws_sdk_braket.types.associations
        out["associations"] = aws_sdk_braket.types.associations.deserialize_json(data["associations"])
    if "experimentalCapabilities" in data:
        import aws_sdk_braket.types.experimental_capabilities
        out["experimental_capabilities"] = aws_sdk_braket.types.experimental_capabilities.deserialize_json(data["experimentalCapabilities"])
    return out