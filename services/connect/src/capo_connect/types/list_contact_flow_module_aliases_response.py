"""Generated from Smithy shape ``com.amazonaws.connect#ListContactFlowModuleAliasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_module_alias_summary_list
    import capo_connect.types.next_token


class ListContactFlowModuleAliasesResponse(TypedDict, closed=True):
    contact_flow_module_alias_summary_list: NotRequired[
        "capo_connect.types.contact_flow_module_alias_summary_list.ContactFlowModuleAliasSummaryList"
    ]
    """<p>Information about the flow module aliases.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactFlowModuleAliasesResponse) -> dict:
    out: dict = {}
    if "contact_flow_module_alias_summary_list" in value:
        import capo_connect.types.contact_flow_module_alias_summary_list

        out["ContactFlowModuleAliasSummaryList"] = (
            capo_connect.types.contact_flow_module_alias_summary_list.serialize_json(
                value["contact_flow_module_alias_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContactFlowModuleAliasesResponse:
    out: ListContactFlowModuleAliasesResponse = {}  # type: ignore[typeddict-item]
    if "ContactFlowModuleAliasSummaryList" in data:
        import capo_connect.types.contact_flow_module_alias_summary_list

        out["contact_flow_module_alias_summary_list"] = (
            capo_connect.types.contact_flow_module_alias_summary_list.deserialize_json(
                data["ContactFlowModuleAliasSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
