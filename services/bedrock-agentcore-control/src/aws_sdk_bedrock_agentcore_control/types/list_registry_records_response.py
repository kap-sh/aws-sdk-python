"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListRegistryRecordsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.next_token
    import aws_sdk_bedrock_agentcore_control.types.registry_record_summary_list


class ListRegistryRecordsResponse(TypedDict):
    registry_records: "aws_sdk_bedrock_agentcore_control.types.registry_record_summary_list.RegistryRecordSummaryList"
    """<p>The list of registry record summaries. For details about the fields in each summary, see the <code>RegistryRecordSummary</code> data type.</p>"""
    next_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.next_token.NextToken"
    ]
    """<p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRegistryRecordsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.registry_record_summary_list

    out["registryRecords"] = (
        aws_sdk_bedrock_agentcore_control.types.registry_record_summary_list.serialize_json(
            value["registry_records"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRegistryRecordsResponse:
    out: ListRegistryRecordsResponse = {}  # type: ignore[typeddict-item]
    if "registryRecords" in data:
        import aws_sdk_bedrock_agentcore_control.types.registry_record_summary_list

        out["registry_records"] = (
            aws_sdk_bedrock_agentcore_control.types.registry_record_summary_list.deserialize_json(
                data["registryRecords"]
            )
        )
    else:
        raise DeserializationError(
            "ListRegistryRecordsResponse.registry_records required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
