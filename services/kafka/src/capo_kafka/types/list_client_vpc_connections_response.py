"""Generated from Smithy shape ``com.amazonaws.kafka#ListClientVpcConnectionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__list_of_client_vpc_connection
    import capo_kafka.types.__string


class ListClientVpcConnectionsResponse(TypedDict, closed=True):
    client_vpc_connections: NotRequired[
        "capo_kafka.types.__list_of_client_vpc_connection.__listOfClientVpcConnection"
    ]
    """<p>List of client VPC connections.</p>"""
    next_token: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The paginated results marker. When the result of a ListClientVpcConnections operation is truncated, the call returns NextToken in the response. To get another batch of configurations, provide this token in your next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClientVpcConnectionsResponse) -> dict:
    out: dict = {}
    if "client_vpc_connections" in value:
        import capo_kafka.types.__list_of_client_vpc_connection

        out["clientVpcConnections"] = (
            capo_kafka.types.__list_of_client_vpc_connection.serialize_json(
                value["client_vpc_connections"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListClientVpcConnectionsResponse:
    out: ListClientVpcConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "clientVpcConnections" in data:
        import capo_kafka.types.__list_of_client_vpc_connection

        out["client_vpc_connections"] = (
            capo_kafka.types.__list_of_client_vpc_connection.deserialize_json(
                data["clientVpcConnections"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
