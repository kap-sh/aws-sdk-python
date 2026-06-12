"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListServiceNetworkVpcAssociationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.service_network_vpc_association_list


class ListServiceNetworkVpcAssociationsResponse(TypedDict):
    items: "aws_sdk_vpc_lattice.types.service_network_vpc_association_list.ServiceNetworkVpcAssociationList"
    """<p>Information about the associations.</p>"""
    next_token: NotRequired["aws_sdk_vpc_lattice.types.next_token.NextToken"]
    """<p>If there are additional results, a pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceNetworkVpcAssociationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_vpc_lattice.types.service_network_vpc_association_list

    out["items"] = (
        aws_sdk_vpc_lattice.types.service_network_vpc_association_list.serialize_json(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceNetworkVpcAssociationsResponse:
    out: ListServiceNetworkVpcAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_vpc_lattice.types.service_network_vpc_association_list

        out["items"] = (
            aws_sdk_vpc_lattice.types.service_network_vpc_association_list.deserialize_json(
                data["items"]
            )
        )
    else:
        raise DeserializationError(
            "ListServiceNetworkVpcAssociationsResponse.items required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
