"""Generated from Smithy shape ``com.amazonaws.odb#OdbNetworkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_odb.types.odb_network_summary

OdbNetworkList: TypeAlias = list["capo_odb.types.odb_network_summary.OdbNetworkSummary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OdbNetworkList) -> list:
    import capo_odb.types.odb_network_summary

    out: list = []
    for item in value:
        out.append(capo_odb.types.odb_network_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> OdbNetworkList:
    import capo_odb.types.odb_network_summary

    out: OdbNetworkList = []
    for item in data:
        out.append(capo_odb.types.odb_network_summary.deserialize_aws_json_1_0(item))
    return out
