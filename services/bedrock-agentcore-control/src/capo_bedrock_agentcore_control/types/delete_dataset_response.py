"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DeleteDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.dataset_arn
    import capo_bedrock_agentcore_control.types.dataset_id
    import capo_bedrock_agentcore_control.types.dataset_status
    import capo_bedrock_agentcore_control.types.dataset_version


class DeleteDatasetResponse(TypedDict, closed=True):
    dataset_arn: "capo_bedrock_agentcore_control.types.dataset_arn.DatasetArn"
    """<p> The Amazon Resource Name (ARN) of the dataset. </p>"""
    dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset. </p>"""
    status: "capo_bedrock_agentcore_control.types.dataset_status.DatasetStatus"
    """<p> The current status of the dataset after the delete request. </p>"""
    dataset_version: (
        "capo_bedrock_agentcore_control.types.dataset_version.DatasetVersion"
    )
    """<p> The version that was deleted. </p>"""
    updated_at: "datetime.datetime"
    """<p> The timestamp when the delete was initiated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDatasetResponse) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    out["datasetId"] = value["dataset_id"]
    import capo_bedrock_agentcore_control.types.dataset_status

    out["status"] = capo_bedrock_agentcore_control.types.dataset_status.serialize_json(
        value["status"]
    )
    out["datasetVersion"] = value["dataset_version"]
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> DeleteDatasetResponse:
    out: DeleteDatasetResponse = {}  # type: ignore[typeddict-item]
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("DeleteDatasetResponse.dataset_arn required")
    if "datasetId" in data:
        out["dataset_id"] = data["datasetId"]
    else:
        raise DeserializationError("DeleteDatasetResponse.dataset_id required")
    if "status" in data:
        import capo_bedrock_agentcore_control.types.dataset_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.dataset_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DeleteDatasetResponse.status required")
    if "datasetVersion" in data:
        out["dataset_version"] = data["datasetVersion"]
    else:
        raise DeserializationError("DeleteDatasetResponse.dataset_version required")
    if "updatedAt" in data:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("DeleteDatasetResponse.updated_at required")
    return out
