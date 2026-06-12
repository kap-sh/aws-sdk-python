"""Generated from Smithy shape ``com.amazonaws.connect#SearchableAgentCriteriaStep``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.agent_resource_id_list
    import aws_sdk_connect.types.search_contacts_match_type


class SearchableAgentCriteriaStep(TypedDict):
    agent_ids: NotRequired[
        "aws_sdk_connect.types.agent_resource_id_list.AgentResourceIdList"
    ]
    """<p>The identifiers of agents used in preferred agents matching.</p>"""
    match_type: NotRequired[
        "aws_sdk_connect.types.search_contacts_match_type.SearchContactsMatchType"
    ]
    """<p>The match type combining multiple agent criteria steps.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchableAgentCriteriaStep) -> dict:
    out: dict = {}
    if "agent_ids" in value:
        import aws_sdk_connect.types.agent_resource_id_list

        out["AgentIds"] = aws_sdk_connect.types.agent_resource_id_list.serialize_json(
            value["agent_ids"]
        )
    if "match_type" in value:
        import aws_sdk_connect.types.search_contacts_match_type

        out["MatchType"] = (
            aws_sdk_connect.types.search_contacts_match_type.serialize_json(
                value["match_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchableAgentCriteriaStep:
    out: SearchableAgentCriteriaStep = {}  # type: ignore[typeddict-item]
    if "AgentIds" in data:
        import aws_sdk_connect.types.agent_resource_id_list

        out["agent_ids"] = (
            aws_sdk_connect.types.agent_resource_id_list.deserialize_json(
                data["AgentIds"]
            )
        )
    if "MatchType" in data:
        import aws_sdk_connect.types.search_contacts_match_type

        out["match_type"] = (
            aws_sdk_connect.types.search_contacts_match_type.deserialize_json(
                data["MatchType"]
            )
        )
    return out
