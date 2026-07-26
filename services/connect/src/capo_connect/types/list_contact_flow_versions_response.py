"""Generated from Smithy shape ``com.amazonaws.connect#ListContactFlowVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_version_summary_list
    import capo_connect.types.next_token


class ListContactFlowVersionsResponse(TypedDict, closed=True):
    contact_flow_version_summary_list: NotRequired[
        "capo_connect.types.contact_flow_version_summary_list.ContactFlowVersionSummaryList"
    ]
    """<p>A list of flow version summaries.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListContactFlowVersionsResponse) -> dict:
    out: dict = {}
    if "contact_flow_version_summary_list" in value:
        import capo_connect.types.contact_flow_version_summary_list

        out["ContactFlowVersionSummaryList"] = (
            capo_connect.types.contact_flow_version_summary_list.serialize_json(
                value["contact_flow_version_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListContactFlowVersionsResponse:
    out: ListContactFlowVersionsResponse = {}  # type: ignore[typeddict-item]
    if "ContactFlowVersionSummaryList" in data:
        import capo_connect.types.contact_flow_version_summary_list

        out["contact_flow_version_summary_list"] = (
            capo_connect.types.contact_flow_version_summary_list.deserialize_json(
                data["ContactFlowVersionSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
