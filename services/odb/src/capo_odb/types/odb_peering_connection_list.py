"""Generated from Smithy shape ``com.amazonaws.odb#OdbPeeringConnectionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.odb_peering_connection_summary

OdbPeeringConnectionList: TypeAlias = list[
    "capo_odb.types.odb_peering_connection_summary.OdbPeeringConnectionSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OdbPeeringConnectionList) -> list:
    import capo_odb.types.odb_peering_connection_summary

    out: list = []
    for item in value:
        out.append(
            capo_odb.types.odb_peering_connection_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> OdbPeeringConnectionList:
    import capo_odb.types.odb_peering_connection_summary

    out: OdbPeeringConnectionList = []
    for item in data:
        out.append(
            capo_odb.types.odb_peering_connection_summary.deserialize_aws_json_1_0(item)
        )
    return out
