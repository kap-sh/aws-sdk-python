"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#FilterInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.branch_filter
    import capo_bedrock_agentcore.types.event_metadata_filter_list


class FilterInput(TypedDict, closed=True):
    branch: NotRequired["capo_bedrock_agentcore.types.branch_filter.BranchFilter"]
    """<p>The branch filter criteria to apply when listing events.</p>"""
    event_metadata: NotRequired[
        "capo_bedrock_agentcore.types.event_metadata_filter_list.EventMetadataFilterList"
    ]
    """<p>Event metadata filter criteria to apply when retrieving events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterInput) -> dict:
    out: dict = {}
    if "branch" in value:
        import capo_bedrock_agentcore.types.branch_filter

        out["branch"] = capo_bedrock_agentcore.types.branch_filter.serialize_json(
            value["branch"]
        )
    if "event_metadata" in value:
        import capo_bedrock_agentcore.types.event_metadata_filter_list

        out["eventMetadata"] = (
            capo_bedrock_agentcore.types.event_metadata_filter_list.serialize_json(
                value["event_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterInput:
    out: FilterInput = {}  # type: ignore[typeddict-item]
    if data.get("branch") is not None:
        import capo_bedrock_agentcore.types.branch_filter

        out["branch"] = capo_bedrock_agentcore.types.branch_filter.deserialize_json(
            data["branch"]
        )
    if data.get("eventMetadata") is not None:
        import capo_bedrock_agentcore.types.event_metadata_filter_list

        out["event_metadata"] = (
            capo_bedrock_agentcore.types.event_metadata_filter_list.deserialize_json(
                data["eventMetadata"]
            )
        )
    return out
