"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfacePermissionList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_interface_permission

NetworkInterfacePermissionList: TypeAlias = list[
    "aws_sdk_ec2.types.network_interface_permission.NetworkInterfacePermission"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInterfacePermissionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.network_interface_permission

        aws_sdk_ec2.types.network_interface_permission.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> NetworkInterfacePermissionList:
    import aws_sdk_ec2.types.network_interface_permission

    out: NetworkInterfacePermissionList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.network_interface_permission.deserialize_ec2_query(child)
        )
    return out
