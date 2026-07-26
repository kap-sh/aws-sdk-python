"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SearchRegistryRecordsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.registry_record_summary_list


class SearchRegistryRecordsResponse(TypedDict, closed=True):
    registry_records: "capo_bedrock_agentcore.types.registry_record_summary_list.RegistryRecordSummaryList"
    """<p> The list of registry records that match the search query, ordered by relevance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchRegistryRecordsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.registry_record_summary_list

    out["registryRecords"] = (
        capo_bedrock_agentcore.types.registry_record_summary_list.serialize_json(
            value["registry_records"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchRegistryRecordsResponse:
    out: SearchRegistryRecordsResponse = {}  # type: ignore[typeddict-item]
    if "registryRecords" in data:
        import capo_bedrock_agentcore.types.registry_record_summary_list

        out["registry_records"] = (
            capo_bedrock_agentcore.types.registry_record_summary_list.deserialize_json(
                data["registryRecords"]
            )
        )
    else:
        raise DeserializationError(
            "SearchRegistryRecordsResponse.registry_records required"
        )
    return out
