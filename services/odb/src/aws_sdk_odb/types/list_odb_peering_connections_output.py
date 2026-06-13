"""Generated from Smithy shape ``com.amazonaws.odb#ListOdbPeeringConnectionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.odb_peering_connection_list


class ListOdbPeeringConnectionsOutput(TypedDict):
    next_token: NotRequired["str"]
    """<p>The pagination token for the next page of ODB peering connections.</p>"""
    odb_peering_connections: (
        "aws_sdk_odb.types.odb_peering_connection_list.OdbPeeringConnectionList"
    )
    """<p>The list of ODB peering connections.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListOdbPeeringConnectionsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_odb.types.odb_peering_connection_list

    out["odbPeeringConnections"] = (
        aws_sdk_odb.types.odb_peering_connection_list.serialize_aws_json_1_0(
            value["odb_peering_connections"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListOdbPeeringConnectionsOutput:
    out: ListOdbPeeringConnectionsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "odbPeeringConnections" in data:
        import aws_sdk_odb.types.odb_peering_connection_list

        out["odb_peering_connections"] = (
            aws_sdk_odb.types.odb_peering_connection_list.deserialize_aws_json_1_0(
                data["odbPeeringConnections"]
            )
        )
    else:
        raise DeserializationError(
            "ListOdbPeeringConnectionsOutput.odb_peering_connections required"
        )
    return out
