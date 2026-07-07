"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DatasetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bedrock_agentcore_control.types.dataset_arn
    import aws_sdk_bedrock_agentcore_control.types.dataset_id
    import aws_sdk_bedrock_agentcore_control.types.dataset_name
    import aws_sdk_bedrock_agentcore_control.types.dataset_schema_type
    import aws_sdk_bedrock_agentcore_control.types.dataset_status
    import aws_sdk_bedrock_agentcore_control.types.draft_status


class DatasetSummary(TypedDict, closed=True):
    dataset_arn: "aws_sdk_bedrock_agentcore_control.types.dataset_arn.DatasetArn"
    """<p> The Amazon Resource Name (ARN) of the dataset. </p>"""
    dataset_id: "aws_sdk_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset. </p>"""
    dataset_name: "aws_sdk_bedrock_agentcore_control.types.dataset_name.DatasetName"
    """<p> The name of the dataset. </p>"""
    description: NotRequired["str"]
    """<p> The description of the dataset. </p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.dataset_status.DatasetStatus"
    """<p> The current status of the dataset. </p>"""
    draft_status: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.draft_status.DraftStatus"
    ]
    """<p> Publish synchronization state. Only authoritative when status is ACTIVE. </p>"""
    schema_type: (
        "aws_sdk_bedrock_agentcore_control.types.dataset_schema_type.DatasetSchemaType"
    )
    """<p> The schema type of the dataset. </p>"""
    example_count: "int"
    """<p> The number of examples in the dataset. </p>"""
    created_at: "datetime.datetime"
    """<p> The timestamp when the dataset was created. </p>"""
    updated_at: "datetime.datetime"
    """<p> The timestamp when the dataset was last updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetSummary) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    out["datasetId"] = value["dataset_id"]
    out["datasetName"] = value["dataset_name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.dataset_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.dataset_status.serialize_json(
            value["status"]
        )
    )
    if "draft_status" in value:
        import aws_sdk_bedrock_agentcore_control.types.draft_status

        out["draftStatus"] = (
            aws_sdk_bedrock_agentcore_control.types.draft_status.serialize_json(
                value["draft_status"]
            )
        )
    import aws_sdk_bedrock_agentcore_control.types.dataset_schema_type

    out["schemaType"] = (
        aws_sdk_bedrock_agentcore_control.types.dataset_schema_type.serialize_json(
            value["schema_type"]
        )
    )
    out["exampleCount"] = value["example_count"]
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> DatasetSummary:
    out: DatasetSummary = {}  # type: ignore[typeddict-item]
    if "datasetArn" in data:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("DatasetSummary.dataset_arn required")
    if "datasetId" in data:
        out["dataset_id"] = data["datasetId"]
    else:
        raise DeserializationError("DatasetSummary.dataset_id required")
    if "datasetName" in data:
        out["dataset_name"] = data["datasetName"]
    else:
        raise DeserializationError("DatasetSummary.dataset_name required")
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.dataset_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.dataset_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DatasetSummary.status required")
    if "draftStatus" in data:
        import aws_sdk_bedrock_agentcore_control.types.draft_status

        out["draft_status"] = (
            aws_sdk_bedrock_agentcore_control.types.draft_status.deserialize_json(
                data["draftStatus"]
            )
        )
    if "schemaType" in data:
        import aws_sdk_bedrock_agentcore_control.types.dataset_schema_type

        out["schema_type"] = (
            aws_sdk_bedrock_agentcore_control.types.dataset_schema_type.deserialize_json(
                data["schemaType"]
            )
        )
    else:
        raise DeserializationError("DatasetSummary.schema_type required")
    if "exampleCount" in data:
        out["example_count"] = data["exampleCount"]
    else:
        raise DeserializationError("DatasetSummary.example_count required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("DatasetSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("DatasetSummary.updated_at required")
    return out
