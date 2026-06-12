"""Generated from Smithy shape ``com.amazonaws.vpclattice#ListResourceGatewaysResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.next_token
    import aws_sdk_vpc_lattice.types.resource_gateway_list


class ListResourceGatewaysResponse(TypedDict):
    items: NotRequired[
        "aws_sdk_vpc_lattice.types.resource_gateway_list.ResourceGatewayList"
    ]
    """<p>Information about the resource gateways.</p>"""
    next_token: NotRequired["aws_sdk_vpc_lattice.types.next_token.NextToken"]
    """<p>If there are additional results, a pagination token for the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceGatewaysResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_vpc_lattice.types.resource_gateway_list

        out["items"] = aws_sdk_vpc_lattice.types.resource_gateway_list.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListResourceGatewaysResponse:
    out: ListResourceGatewaysResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_vpc_lattice.types.resource_gateway_list

        out["items"] = aws_sdk_vpc_lattice.types.resource_gateway_list.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
