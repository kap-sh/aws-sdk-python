"""Generated from Smithy shape ``com.amazonaws.directconnect#AllocateHostedConnectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.bandwidth
    import aws_sdk_direct_connect.types.connection_id
    import aws_sdk_direct_connect.types.connection_name
    import aws_sdk_direct_connect.types.owner_account
    import aws_sdk_direct_connect.types.tag_list
    import aws_sdk_direct_connect.types.vlan


class AllocateHostedConnectionRequest(TypedDict, closed=True):
    connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the interconnect or LAG.</p>"""
    owner_account: "aws_sdk_direct_connect.types.owner_account.OwnerAccount"
    """<p>The ID of the Amazon Web Services account ID of the customer for the connection.</p>"""
    bandwidth: "aws_sdk_direct_connect.types.bandwidth.Bandwidth"
    """<p>The bandwidth of the connection. The possible values are 50Mbps, 100Mbps, 200Mbps, 300Mbps, 400Mbps, 500Mbps, 1Gbps, 2Gbps, 5Gbps, 10Gbps, and 25Gbps. Note that only those Direct Connect Partners who have met specific requirements are allowed to create a 1Gbps, 2Gbps, 5Gbps, 10Gbps, or 25Gbps hosted connection. </p>"""
    connection_name: "aws_sdk_direct_connect.types.connection_name.ConnectionName"
    """<p>The name of the hosted connection.</p>"""
    vlan: "aws_sdk_direct_connect.types.vlan.VLAN"
    """<p>The dedicated VLAN provisioned to the hosted connection.</p>"""
    tags: NotRequired["aws_sdk_direct_connect.types.tag_list.TagList"]
    """<p>The tags associated with the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AllocateHostedConnectionRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    out["ownerAccount"] = value["owner_account"]
    out["bandwidth"] = value["bandwidth"]
    out["connectionName"] = value["connection_name"]
    out["vlan"] = value.get("vlan", 0)
    if "tags" in value:
        import aws_sdk_direct_connect.types.tag_list

        out["tags"] = aws_sdk_direct_connect.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AllocateHostedConnectionRequest:
    out: AllocateHostedConnectionRequest = {}  # type: ignore[typeddict-item]
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    else:
        raise DeserializationError(
            "AllocateHostedConnectionRequest.connection_id required"
        )
    if "ownerAccount" in data:
        out["owner_account"] = data["ownerAccount"]
    else:
        raise DeserializationError(
            "AllocateHostedConnectionRequest.owner_account required"
        )
    if "bandwidth" in data:
        out["bandwidth"] = data["bandwidth"]
    else:
        raise DeserializationError("AllocateHostedConnectionRequest.bandwidth required")
    if "connectionName" in data:
        out["connection_name"] = data["connectionName"]
    else:
        raise DeserializationError(
            "AllocateHostedConnectionRequest.connection_name required"
        )
    if "vlan" in data:
        out["vlan"] = data["vlan"]
    else:
        out["vlan"] = 0
    if "tags" in data:
        import aws_sdk_direct_connect.types.tag_list

        out["tags"] = aws_sdk_direct_connect.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
