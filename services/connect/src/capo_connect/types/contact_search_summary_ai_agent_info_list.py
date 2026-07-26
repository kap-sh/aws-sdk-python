"""Generated from Smithy shape ``com.amazonaws.connect#ContactSearchSummaryAiAgentInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.contact_search_summary_ai_agent_info

ContactSearchSummaryAiAgentInfoList: TypeAlias = list[
    "capo_connect.types.contact_search_summary_ai_agent_info.ContactSearchSummaryAiAgentInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactSearchSummaryAiAgentInfoList) -> list:
    import capo_connect.types.contact_search_summary_ai_agent_info

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.contact_search_summary_ai_agent_info.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ContactSearchSummaryAiAgentInfoList:
    import capo_connect.types.contact_search_summary_ai_agent_info

    out: ContactSearchSummaryAiAgentInfoList = []
    for item in data:
        out.append(
            capo_connect.types.contact_search_summary_ai_agent_info.deserialize_json(
                item
            )
        )
    return out
