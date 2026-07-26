"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListServiceNetworkServiceAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import capo_vpc_lattice.types.next_token
    import capo_vpc_lattice.types.service_network_service_association_list


class ListServiceNetworkServiceAssociationsResponse(TypedDict, closed=True):
    items: "capo_vpc_lattice.types.service_network_service_association_list.ServiceNetworkServiceAssociationList"
    """<p>Information about the associations.</p>"""
    next_token: NotRequired["capo_vpc_lattice.types.next_token.NextToken"]
    """<p>If there are additional results, a pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceNetworkServiceAssociationsResponse) -> dict:
    out: dict = {}
    import capo_vpc_lattice.types.service_network_service_association_list

    out["items"] = (
        capo_vpc_lattice.types.service_network_service_association_list.serialize_json(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceNetworkServiceAssociationsResponse:
    out: ListServiceNetworkServiceAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_vpc_lattice.types.service_network_service_association_list

        out["items"] = (
            capo_vpc_lattice.types.service_network_service_association_list.deserialize_json(
                data["items"]
            )
        )
    else:
        raise DeserializationError(
            "ListServiceNetworkServiceAssociationsResponse.items required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
