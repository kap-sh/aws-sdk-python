"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabasePeerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_odb.types.autonomous_database_peer_summary

AutonomousDatabasePeerList: TypeAlias = list[
    "aws_sdk_odb.types.autonomous_database_peer_summary.AutonomousDatabasePeerSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabasePeerList) -> list:
    import aws_sdk_odb.types.autonomous_database_peer_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_odb.types.autonomous_database_peer_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AutonomousDatabasePeerList:
    import aws_sdk_odb.types.autonomous_database_peer_summary

    out: AutonomousDatabasePeerList = []
    for item in data:
        out.append(
            aws_sdk_odb.types.autonomous_database_peer_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
