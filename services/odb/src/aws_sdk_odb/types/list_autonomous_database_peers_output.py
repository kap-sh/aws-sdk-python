"""Generated from Smithy shape ``com.amazonaws.odb#ListAutonomousDatabasePeersOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.autonomous_database_peer_list


class ListAutonomousDatabasePeersOutput(TypedDict):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    autonomous_database_peers: (
        "aws_sdk_odb.types.autonomous_database_peer_list.AutonomousDatabasePeerList"
    )
    """<p>The list of peer databases for the Autonomous Database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutonomousDatabasePeersOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_odb.types.autonomous_database_peer_list

    out["autonomousDatabasePeers"] = (
        aws_sdk_odb.types.autonomous_database_peer_list.serialize_aws_json_1_0(
            value["autonomous_database_peers"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutonomousDatabasePeersOutput:
    out: ListAutonomousDatabasePeersOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "autonomousDatabasePeers" in data:
        import aws_sdk_odb.types.autonomous_database_peer_list

        out["autonomous_database_peers"] = (
            aws_sdk_odb.types.autonomous_database_peer_list.deserialize_aws_json_1_0(
                data["autonomousDatabasePeers"]
            )
        )
    else:
        raise DeserializationError(
            "ListAutonomousDatabasePeersOutput.autonomous_database_peers required"
        )
    return out
