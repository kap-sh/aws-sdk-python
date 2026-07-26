"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DatasetVersionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.dataset_version_summary

DatasetVersionSummaryList: TypeAlias = list[
    "capo_bedrock_agentcore_control.types.dataset_version_summary.DatasetVersionSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetVersionSummaryList) -> list:
    import capo_bedrock_agentcore_control.types.dataset_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_agentcore_control.types.dataset_version_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DatasetVersionSummaryList:
    import capo_bedrock_agentcore_control.types.dataset_version_summary

    out: DatasetVersionSummaryList = []
    for item in data:
        out.append(
            capo_bedrock_agentcore_control.types.dataset_version_summary.deserialize_json(
                item
            )
        )
    return out
