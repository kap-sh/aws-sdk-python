"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateDatasetExamplesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.dataset_arn
    import capo_bedrock_agentcore_control.types.dataset_id
    import capo_bedrock_agentcore_control.types.dataset_status


class UpdateDatasetExamplesResponse(TypedDict, closed=True):
    dataset_arn: "capo_bedrock_agentcore_control.types.dataset_arn.DatasetArn"
    """<p> The Amazon Resource Name (ARN) of the dataset. </p>"""
    dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset. </p>"""
    status: "capo_bedrock_agentcore_control.types.dataset_status.DatasetStatus"
    """<p> The current status of the dataset. </p>"""
    updated_count: "int"
    """<p> The number of examples updated. </p>"""
    updated_at: "datetime.datetime"
    """<p> The timestamp when the examples were updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDatasetExamplesResponse) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    out["datasetId"] = value["dataset_id"]
    import capo_bedrock_agentcore_control.types.dataset_status

    out["status"] = capo_bedrock_agentcore_control.types.dataset_status.serialize_json(
        value["status"]
    )
    out["updatedCount"] = value["updated_count"]
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateDatasetExamplesResponse:
    out: UpdateDatasetExamplesResponse = {}  # type: ignore[typeddict-item]
    if data.get("datasetArn") is not None:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("UpdateDatasetExamplesResponse.dataset_arn required")
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        raise DeserializationError("UpdateDatasetExamplesResponse.dataset_id required")
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.dataset_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.dataset_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateDatasetExamplesResponse.status required")
    if data.get("updatedCount") is not None:
        out["updated_count"] = data["updatedCount"]
    else:
        raise DeserializationError(
            "UpdateDatasetExamplesResponse.updated_count required"
        )
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("UpdateDatasetExamplesResponse.updated_at required")
    return out
