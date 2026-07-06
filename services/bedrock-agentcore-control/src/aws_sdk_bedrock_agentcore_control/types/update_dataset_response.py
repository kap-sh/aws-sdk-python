"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore_control.types.dataset_arn
    import aws_sdk_bedrock_agentcore_control.types.dataset_id


class UpdateDatasetResponse(TypedDict, closed=True):
    dataset_arn: "aws_sdk_bedrock_agentcore_control.types.dataset_arn.DatasetArn"
    """<p> The Amazon Resource Name (ARN) of the updated dataset. </p>"""
    dataset_id: "aws_sdk_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the updated dataset. </p>"""
    updated_at: "datetime.datetime"
    """<p> The timestamp when the dataset was updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDatasetResponse) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    out["datasetId"] = value["dataset_id"]
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateDatasetResponse:
    out: UpdateDatasetResponse = {}  # type: ignore[typeddict-item]
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("UpdateDatasetResponse.dataset_arn required")
    if "datasetId" in data:
        out["dataset_id"] = data["datasetId"]
    else:
        raise DeserializationError("UpdateDatasetResponse.dataset_id required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("UpdateDatasetResponse.updated_at required")
    return out
