"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DatasetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.dataset_arn
    import capo_bedrock_agentcore_control.types.dataset_id
    import capo_bedrock_agentcore_control.types.dataset_name
    import capo_bedrock_agentcore_control.types.dataset_schema_type
    import capo_bedrock_agentcore_control.types.dataset_status
    import capo_bedrock_agentcore_control.types.draft_status


class DatasetSummary(TypedDict, closed=True):
    dataset_arn: "capo_bedrock_agentcore_control.types.dataset_arn.DatasetArn"
    """<p> The Amazon Resource Name (ARN) of the dataset. </p>"""
    dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId"
    """<p> The unique identifier of the dataset. </p>"""
    dataset_name: "capo_bedrock_agentcore_control.types.dataset_name.DatasetName"
    """<p> The name of the dataset. </p>"""
    description: NotRequired["str"]
    """<p> The description of the dataset. </p>"""
    status: "capo_bedrock_agentcore_control.types.dataset_status.DatasetStatus"
    """<p> The current status of the dataset. </p>"""
    draft_status: NotRequired[
        "capo_bedrock_agentcore_control.types.draft_status.DraftStatus"
    ]
    """<p> Publish synchronization state. Only authoritative when status is ACTIVE. </p>"""
    schema_type: (
        "capo_bedrock_agentcore_control.types.dataset_schema_type.DatasetSchemaType"
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
    import capo_bedrock_agentcore_control.types.dataset_status

    out["status"] = capo_bedrock_agentcore_control.types.dataset_status.serialize_json(
        value["status"]
    )
    if "draft_status" in value:
        import capo_bedrock_agentcore_control.types.draft_status

        out["draftStatus"] = (
            capo_bedrock_agentcore_control.types.draft_status.serialize_json(
                value["draft_status"]
            )
        )
    import capo_bedrock_agentcore_control.types.dataset_schema_type

    out["schemaType"] = (
        capo_bedrock_agentcore_control.types.dataset_schema_type.serialize_json(
            value["schema_type"]
        )
    )
    out["exampleCount"] = value["example_count"]
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> DatasetSummary:
    out: DatasetSummary = {}  # type: ignore[typeddict-item]
    if data.get("datasetArn") is not None:
        out["dataset_arn"] = data["datasetArn"]
    else:
        raise DeserializationError("DatasetSummary.dataset_arn required")
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        raise DeserializationError("DatasetSummary.dataset_id required")
    if data.get("datasetName") is not None:
        out["dataset_name"] = data["datasetName"]
    else:
        raise DeserializationError("DatasetSummary.dataset_name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.dataset_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.dataset_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DatasetSummary.status required")
    if data.get("draftStatus") is not None:
        import capo_bedrock_agentcore_control.types.draft_status

        out["draft_status"] = (
            capo_bedrock_agentcore_control.types.draft_status.deserialize_json(
                data["draftStatus"]
            )
        )
    if data.get("schemaType") is not None:
        import capo_bedrock_agentcore_control.types.dataset_schema_type

        out["schema_type"] = (
            capo_bedrock_agentcore_control.types.dataset_schema_type.deserialize_json(
                data["schemaType"]
            )
        )
    else:
        raise DeserializationError("DatasetSummary.schema_type required")
    if data.get("exampleCount") is not None:
        out["example_count"] = data["exampleCount"]
    else:
        raise DeserializationError("DatasetSummary.example_count required")
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("DatasetSummary.created_at required")
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("DatasetSummary.updated_at required")
    return out
