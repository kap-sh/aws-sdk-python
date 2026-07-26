"""Generated from Smithy shape ``com.amazonaws.odb#AutonomousDatabasePeerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.autonomous_database_peer_summary

AutonomousDatabasePeerList: TypeAlias = list[
    "capo_odb.types.autonomous_database_peer_summary.AutonomousDatabasePeerSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutonomousDatabasePeerList) -> list:
    import capo_odb.types.autonomous_database_peer_summary

    out: list = []
    for item in value:
        out.append(
            capo_odb.types.autonomous_database_peer_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AutonomousDatabasePeerList:
    import capo_odb.types.autonomous_database_peer_summary

    out: AutonomousDatabasePeerList = []
    for item in data:
        out.append(
            capo_odb.types.autonomous_database_peer_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
