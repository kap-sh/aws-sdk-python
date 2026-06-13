"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteDatasetExamplesResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.dataset_arn
    import aws_sdk_bedrock_agentcore_control.types.dataset_id
    import aws_sdk_bedrock_agentcore_control.types.dataset_status
    import datetime

class DeleteDatasetExamplesResponse(TypedDict):
    dataset_arn: "aws_sdk_bedrock_agentcore_control.types.dataset_arn.DatasetArn"
    """<p> The Amazon Resource Name (ARN) of the dataset. </p>"""
    dataset_id: "aws_sdk_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset. </p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.dataset_status.DatasetStatus"
    """<p> The current status of the dataset. </p>"""
    deleted_count: "int"
    """<p> The number of examples deleted. </p>"""
    updated_at: "datetime.datetime"
    """<p> The timestamp when the examples were deleted. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteDatasetExamplesResponse) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    out["datasetId"] = value["dataset_id"]
    import aws_sdk_bedrock_agentcore_control.types.dataset_status
    out["status"] = aws_sdk_bedrock_agentcore_control.types.dataset_status.serialize_json(value["status"])
    out["deletedCount"] = value["deleted_count"]
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp
    out["updatedAt"] = aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(value["updated_at"])
    return out


def deserialize_json(data: dict) -> DeleteDatasetExamplesResponse:
    out: DeleteDatasetExamplesResponse = {}  # type: ignore[typeddict-item]
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("DeleteDatasetExamplesResponse.dataset_arn required")
    if "datasetId" in data:
        out["dataset_id"] = data["datasetId"]
    else:
        raise DeserializationError("DeleteDatasetExamplesResponse.dataset_id required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.dataset_status
        out["status"] = aws_sdk_bedrock_agentcore_control.types.dataset_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("DeleteDatasetExamplesResponse.status required")
    if "deletedCount" in data:
        out["deleted_count"] = data["deletedCount"]
    else:
        raise DeserializationError("DeleteDatasetExamplesResponse.deleted_count required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp
        out["updated_at"] = aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(data["updatedAt"])
    else:
        raise DeserializationError("DeleteDatasetExamplesResponse.updated_at required")
    return out