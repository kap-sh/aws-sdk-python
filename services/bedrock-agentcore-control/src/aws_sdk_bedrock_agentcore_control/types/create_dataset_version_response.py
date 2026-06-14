"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateDatasetVersionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore_control.types.dataset_arn
    import aws_sdk_bedrock_agentcore_control.types.dataset_id
    import aws_sdk_bedrock_agentcore_control.types.dataset_status
    import aws_sdk_bedrock_agentcore_control.types.dataset_version


class CreateDatasetVersionResponse(TypedDict):
    dataset_arn: "aws_sdk_bedrock_agentcore_control.types.dataset_arn.DatasetArn"
    """<p> The Amazon Resource Name (ARN) of the dataset. </p>"""
    dataset_id: "aws_sdk_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset. </p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.dataset_status.DatasetStatus"
    """<p> Always UPDATING immediately after this call. Poll <code>GetDataset</code> until status transitions to ACTIVE or UPDATE_FAILED. </p>"""
    dataset_version: (
        "aws_sdk_bedrock_agentcore_control.types.dataset_version.DatasetVersion"
    )
    """<p> The version number being created. </p>"""
    created_at: "datetime.datetime"
    """<p> The timestamp when the version creation was initiated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatasetVersionResponse) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    out["datasetId"] = value["dataset_id"]
    import aws_sdk_bedrock_agentcore_control.types.dataset_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.dataset_status.serialize_json(
            value["status"]
        )
    )
    out["datasetVersion"] = value["dataset_version"]
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateDatasetVersionResponse:
    out: CreateDatasetVersionResponse = {}  # type: ignore[typeddict-item]
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("CreateDatasetVersionResponse.dataset_arn required")
    if "datasetId" in data:
        out["dataset_id"] = data["datasetId"]
    else:
        raise DeserializationError("CreateDatasetVersionResponse.dataset_id required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.dataset_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.dataset_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateDatasetVersionResponse.status required")
    if "datasetVersion" in data:
        out["dataset_version"] = data["datasetVersion"]
    else:
        raise DeserializationError(
            "CreateDatasetVersionResponse.dataset_version required"
        )
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("CreateDatasetVersionResponse.created_at required")
    return out
