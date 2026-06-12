"""Generated from Smithy shape ``com.amazonaws.kafka#ListVpcConnectionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of_vpc_connection
    import aws_sdk_kafka.types.__string


class ListVpcConnectionsResponse(TypedDict):
    vpc_connections: NotRequired[
        "aws_sdk_kafka.types.__list_of_vpc_connection.__listOfVpcConnection"
    ]
    """<p>List of VPC connections.</p>"""
    next_token: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The paginated results marker. When the result of a ListClientVpcConnections operation is truncated, the call returns NextToken in the response. To get another batch of configurations, provide this token in your next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVpcConnectionsResponse) -> dict:
    out: dict = {}
    if "vpc_connections" in value:
        import aws_sdk_kafka.types.__list_of_vpc_connection

        out["vpcConnections"] = (
            aws_sdk_kafka.types.__list_of_vpc_connection.serialize_json(
                value["vpc_connections"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListVpcConnectionsResponse:
    out: ListVpcConnectionsResponse = {}  # type: ignore[typeddict-item]
    if "vpcConnections" in data:
        import aws_sdk_kafka.types.__list_of_vpc_connection

        out["vpc_connections"] = (
            aws_sdk_kafka.types.__list_of_vpc_connection.deserialize_json(
                data["vpcConnections"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
