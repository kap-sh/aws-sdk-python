"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DatasetVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bedrock_agentcore_control.types.dataset_version


class DatasetVersionSummary(TypedDict, closed=True):
    dataset_version: (
        "capo_bedrock_agentcore_control.types.dataset_version.DatasetVersion"
    )
    """<p> The version number of this published snapshot. </p>"""
    example_count: "int"
    """<p> The number of examples in this version. </p>"""
    created_at: "datetime.datetime"
    """<p> The timestamp when this version was published. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatasetVersionSummary) -> dict:
    out: dict = {}
    out["datasetVersion"] = value["dataset_version"]
    out["exampleCount"] = value["example_count"]
    import capo_bedrock_agentcore_control.types._prelude.timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    )
    return out


def deserialize_json(data: dict) -> DatasetVersionSummary:
    out: DatasetVersionSummary = {}  # type: ignore[typeddict-item]
    if "datasetVersion" in data:
        out["dataset_version"] = data["datasetVersion"]
    else:
        raise DeserializationError("DatasetVersionSummary.dataset_version required")
    if "exampleCount" in data:
        out["example_count"] = data["exampleCount"]
    else:
        raise DeserializationError("DatasetVersionSummary.example_count required")
    if "createdAt" in data:
        import capo_bedrock_agentcore_control.types._prelude.timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("DatasetVersionSummary.created_at required")
    return out
