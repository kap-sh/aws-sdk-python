"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AddDatasetExamplesResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.dataset_arn
    import aws_sdk_bedrock_agentcore_control.types.dataset_id
    import aws_sdk_bedrock_agentcore_control.types.dataset_status
    import aws_sdk_bedrock_agentcore_control.types.example_id_list
    import datetime

class AddDatasetExamplesResponse(TypedDict):
    dataset_arn: "aws_sdk_bedrock_agentcore_control.types.dataset_arn.DatasetArn"
    """<p> The Amazon Resource Name (ARN) of the dataset. </p>"""
    dataset_id: "aws_sdk_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset. </p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.dataset_status.DatasetStatus"
    """<p> The current status of the dataset. </p>"""
    added_count: "int"
    """<p> The number of examples added. </p>"""
    updated_at: "datetime.datetime"
    """<p> The timestamp when the examples were added. </p>"""
    example_ids: "aws_sdk_bedrock_agentcore_control.types.example_id_list.ExampleIdList"
    """<p> IDs of all added examples (auto-generated UUIDs). </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AddDatasetExamplesResponse) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    out["datasetId"] = value["dataset_id"]
    import aws_sdk_bedrock_agentcore_control.types.dataset_status
    out["status"] = aws_sdk_bedrock_agentcore_control.types.dataset_status.serialize_json(value["status"])
    out["addedCount"] = value["added_count"]
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp
    out["updatedAt"] = aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(value["updated_at"])
    import aws_sdk_bedrock_agentcore_control.types.example_id_list
    out["exampleIds"] = aws_sdk_bedrock_agentcore_control.types.example_id_list.serialize_json(value["example_ids"])
    return out


def deserialize_json(data: dict) -> AddDatasetExamplesResponse:
    out: AddDatasetExamplesResponse = {}  # type: ignore[typeddict-item]
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("AddDatasetExamplesResponse.dataset_arn required")
    if "datasetId" in data:
        out["dataset_id"] = data["datasetId"]
    else:
        raise DeserializationError("AddDatasetExamplesResponse.dataset_id required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.dataset_status
        out["status"] = aws_sdk_bedrock_agentcore_control.types.dataset_status.deserialize_json(data["status"])
    else:
        raise DeserializationError("AddDatasetExamplesResponse.status required")
    if "addedCount" in data:
        out["added_count"] = data["addedCount"]
    else:
        raise DeserializationError("AddDatasetExamplesResponse.added_count required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp
        out["updated_at"] = aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(data["updatedAt"])
    else:
        raise DeserializationError("AddDatasetExamplesResponse.updated_at required")
    if "exampleIds" in data:
        import aws_sdk_bedrock_agentcore_control.types.example_id_list
        out["example_ids"] = aws_sdk_bedrock_agentcore_control.types.example_id_list.deserialize_json(data["exampleIds"])
    else:
        raise DeserializationError("AddDatasetExamplesResponse.example_ids required")
    return out