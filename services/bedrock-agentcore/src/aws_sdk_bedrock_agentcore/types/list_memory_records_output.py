"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ListMemoryRecordsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.memory_record_summary_list
    import aws_sdk_bedrock_agentcore.types.pagination_token


class ListMemoryRecordsOutput(TypedDict, closed=True):
    memory_record_summaries: "aws_sdk_bedrock_agentcore.types.memory_record_summary_list.MemoryRecordSummaryList"
    """<p>The list of memory record summaries that match the specified criteria.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use in a subsequent request to get the next set of results. This value is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMemoryRecordsOutput) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.memory_record_summary_list

    out["memoryRecordSummaries"] = (
        aws_sdk_bedrock_agentcore.types.memory_record_summary_list.serialize_json(
            value["memory_record_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListMemoryRecordsOutput:
    out: ListMemoryRecordsOutput = {}  # type: ignore[typeddict-item]
    if "memoryRecordSummaries" in data:
        import aws_sdk_bedrock_agentcore.types.memory_record_summary_list

        out["memory_record_summaries"] = (
            aws_sdk_bedrock_agentcore.types.memory_record_summary_list.deserialize_json(
                data["memoryRecordSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListMemoryRecordsOutput.memory_record_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
