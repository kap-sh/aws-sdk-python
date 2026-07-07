"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListResourceEndpointAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.resource_endpoint_association_list


class ListResourceEndpointAssociationsResponse(TypedDict, closed=True):
    items: "aws_sdk_vpc_lattice.types.resource_endpoint_association_list.ResourceEndpointAssociationList"
    """<p>Information about the VPC endpoint associations.</p>"""
    next_token: NotRequired["aws_sdk_vpc_lattice.types.next_token.NextToken"]
    """<p>If there are additional results, a pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceEndpointAssociationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_vpc_lattice.types.resource_endpoint_association_list

    out["items"] = (
        aws_sdk_vpc_lattice.types.resource_endpoint_association_list.serialize_json(
            value["items"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourceEndpointAssociationsResponse:
    out: ListResourceEndpointAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_vpc_lattice.types.resource_endpoint_association_list

        out["items"] = (
            aws_sdk_vpc_lattice.types.resource_endpoint_association_list.deserialize_json(
                data["items"]
            )
        )
    else:
        raise DeserializationError(
            "ListResourceEndpointAssociationsResponse.items required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
