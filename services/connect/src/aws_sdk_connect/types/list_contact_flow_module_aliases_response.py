"""Generated from Smithy shape ``com.amazonaws.connect#ListContactFlowModuleAliasesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_module_alias_summary_list
    import aws_sdk_connect.types.next_token


class ListContactFlowModuleAliasesResponse(TypedDict):
    contact_flow_module_alias_summary_list: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_alias_summary_list.ContactFlowModuleAliasSummaryList"
    ]
    """<p>Information about the flow module aliases.</p>"""
    next_token: NotRequired["aws_sdk_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactFlowModuleAliasesResponse) -> dict:
    out: dict = {}
    if "contact_flow_module_alias_summary_list" in value:
        import aws_sdk_connect.types.contact_flow_module_alias_summary_list

        out["ContactFlowModuleAliasSummaryList"] = (
            aws_sdk_connect.types.contact_flow_module_alias_summary_list.serialize_json(
                value["contact_flow_module_alias_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContactFlowModuleAliasesResponse:
    out: ListContactFlowModuleAliasesResponse = {}  # type: ignore[typeddict-item]
    if "ContactFlowModuleAliasSummaryList" in data:
        import aws_sdk_connect.types.contact_flow_module_alias_summary_list

        out["contact_flow_module_alias_summary_list"] = (
            aws_sdk_connect.types.contact_flow_module_alias_summary_list.deserialize_json(
                data["ContactFlowModuleAliasSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
