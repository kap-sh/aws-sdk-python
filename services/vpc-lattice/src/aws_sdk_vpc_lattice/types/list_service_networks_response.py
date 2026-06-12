"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListServiceNetworksResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_vpc_lattice.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.service_network_list


class ListServiceNetworksResponse(TypedDict):
    items: "aws_sdk_vpc_lattice.types.service_network_list.ServiceNetworkList"
    """<p>Information about the service networks.</p>"""
    next_token: NotRequired["aws_sdk_vpc_lattice.types.next_token.NextToken"]
    """<p>If there are additional results, a pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServiceNetworksResponse) -> dict:
    out: dict = {}
    import aws_sdk_vpc_lattice.types.service_network_list

    out["items"] = aws_sdk_vpc_lattice.types.service_network_list.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListServiceNetworksResponse:
    out: ListServiceNetworksResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_vpc_lattice.types.service_network_list

        out["items"] = aws_sdk_vpc_lattice.types.service_network_list.deserialize_json(
            data["items"]
        )
    else:
        raise DeserializationError("ListServiceNetworksResponse.items required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
