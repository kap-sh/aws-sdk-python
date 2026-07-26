"""Generated from Smithy shape ``com.amazonaws.connect#ListIntegrationAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.integration_association_summary_list
    import capo_connect.types.next_token


class ListIntegrationAssociationsResponse(TypedDict, closed=True):
    integration_association_summary_list: NotRequired[
        "capo_connect.types.integration_association_summary_list.IntegrationAssociationSummaryList"
    ]
    """<p>The associations.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIntegrationAssociationsResponse) -> dict:
    out: dict = {}
    if "integration_association_summary_list" in value:
        import capo_connect.types.integration_association_summary_list

        out["IntegrationAssociationSummaryList"] = (
            capo_connect.types.integration_association_summary_list.serialize_json(
                value["integration_association_summary_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIntegrationAssociationsResponse:
    out: ListIntegrationAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "IntegrationAssociationSummaryList" in data:
        import capo_connect.types.integration_association_summary_list

        out["integration_association_summary_list"] = (
            capo_connect.types.integration_association_summary_list.deserialize_json(
                data["IntegrationAssociationSummaryList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
