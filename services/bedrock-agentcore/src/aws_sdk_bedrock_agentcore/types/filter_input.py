"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#FilterInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.branch_filter
    import aws_sdk_bedrock_agentcore.types.event_metadata_filter_list


class FilterInput(TypedDict):
    branch: NotRequired["aws_sdk_bedrock_agentcore.types.branch_filter.BranchFilter"]
    """<p>The branch filter criteria to apply when listing events.</p>"""
    event_metadata: NotRequired[
        "aws_sdk_bedrock_agentcore.types.event_metadata_filter_list.EventMetadataFilterList"
    ]
    """<p>Event metadata filter criteria to apply when retrieving events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterInput) -> dict:
    out: dict = {}
    if "branch" in value:
        import aws_sdk_bedrock_agentcore.types.branch_filter

        out["branch"] = aws_sdk_bedrock_agentcore.types.branch_filter.serialize_json(
            value["branch"]
        )
    if "event_metadata" in value:
        import aws_sdk_bedrock_agentcore.types.event_metadata_filter_list

        out["eventMetadata"] = (
            aws_sdk_bedrock_agentcore.types.event_metadata_filter_list.serialize_json(
                value["event_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterInput:
    out: FilterInput = {}  # type: ignore[typeddict-item]
    if "branch" in data:
        import aws_sdk_bedrock_agentcore.types.branch_filter

        out["branch"] = aws_sdk_bedrock_agentcore.types.branch_filter.deserialize_json(
            data["branch"]
        )
    if "eventMetadata" in data:
        import aws_sdk_bedrock_agentcore.types.event_metadata_filter_list

        out["event_metadata"] = (
            aws_sdk_bedrock_agentcore.types.event_metadata_filter_list.deserialize_json(
                data["eventMetadata"]
            )
        )
    return out
