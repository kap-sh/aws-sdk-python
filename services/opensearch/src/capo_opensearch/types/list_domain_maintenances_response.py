"""Generated from Smithy shape ``com.amazonaws.opensearch#ListDomainMaintenancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.domain_maintenance_list
    import capo_opensearch.types.next_token


class ListDomainMaintenancesResponse(TypedDict, closed=True):
    domain_maintenances: NotRequired[
        "capo_opensearch.types.domain_maintenance_list.DomainMaintenanceList"
    ]
    """<p>A list of the submitted maintenance actions.</p>"""
    next_token: NotRequired["capo_opensearch.types.next_token.NextToken"]
    """<p>When <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainMaintenancesResponse) -> dict:
    out: dict = {}
    if "domain_maintenances" in value:
        import capo_opensearch.types.domain_maintenance_list

        out["DomainMaintenances"] = (
            capo_opensearch.types.domain_maintenance_list.serialize_json(
                value["domain_maintenances"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDomainMaintenancesResponse:
    out: ListDomainMaintenancesResponse = {}  # type: ignore[typeddict-item]
    if "DomainMaintenances" in data:
        import capo_opensearch.types.domain_maintenance_list

        out["domain_maintenances"] = (
            capo_opensearch.types.domain_maintenance_list.deserialize_json(
                data["DomainMaintenances"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
