"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SearchRegistryRecordsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.registry_record_summary_list


class SearchRegistryRecordsResponse(TypedDict):
    registry_records: "aws_sdk_bedrock_agentcore.types.registry_record_summary_list.RegistryRecordSummaryList"
    """<p> The list of registry records that match the search query, ordered by relevance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchRegistryRecordsResponse) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.registry_record_summary_list

    out["registryRecords"] = (
        aws_sdk_bedrock_agentcore.types.registry_record_summary_list.serialize_json(
            value["registry_records"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchRegistryRecordsResponse:
    out: SearchRegistryRecordsResponse = {}  # type: ignore[typeddict-item]
    if "registryRecords" in data:
        import aws_sdk_bedrock_agentcore.types.registry_record_summary_list

        out["registry_records"] = (
            aws_sdk_bedrock_agentcore.types.registry_record_summary_list.deserialize_json(
                data["registryRecords"]
            )
        )
    else:
        raise DeserializationError(
            "SearchRegistryRecordsResponse.registry_records required"
        )
    return out
