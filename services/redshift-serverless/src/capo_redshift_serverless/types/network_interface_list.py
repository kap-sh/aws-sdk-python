"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#NetworkInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_redshift_serverless.types.network_interface

NetworkInterfaceList: TypeAlias = list[
    "capo_redshift_serverless.types.network_interface.NetworkInterface"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkInterfaceList) -> list:
    import capo_redshift_serverless.types.network_interface

    out: list = []
    for item in value:
        out.append(
            capo_redshift_serverless.types.network_interface.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NetworkInterfaceList:
    import capo_redshift_serverless.types.network_interface

    out: NetworkInterfaceList = []
    for item in data:
        out.append(
            capo_redshift_serverless.types.network_interface.deserialize_aws_json_1_1(
                item
            )
        )
    return out
