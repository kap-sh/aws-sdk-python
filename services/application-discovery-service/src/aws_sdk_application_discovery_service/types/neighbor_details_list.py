"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#NeighborDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_discovery_service.types.neighbor_connection_detail

NeighborDetailsList: TypeAlias = list[
    "aws_sdk_application_discovery_service.types.neighbor_connection_detail.NeighborConnectionDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NeighborDetailsList) -> list:
    import aws_sdk_application_discovery_service.types.neighbor_connection_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_application_discovery_service.types.neighbor_connection_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NeighborDetailsList:
    import aws_sdk_application_discovery_service.types.neighbor_connection_detail

    out: NeighborDetailsList = []
    for item in data:
        out.append(
            aws_sdk_application_discovery_service.types.neighbor_connection_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
