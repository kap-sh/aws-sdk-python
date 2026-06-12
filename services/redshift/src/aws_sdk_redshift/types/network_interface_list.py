"""Generated from Smithy shape ``com.amazonaws.redshift#NetworkInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.network_interface

NetworkInterfaceList: TypeAlias = list[
    "aws_sdk_redshift.types.network_interface.NetworkInterface"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: NetworkInterfaceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.network_interface

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.network_interface.serialize_query(
            item, pairs, f"{prefix}.NetworkInterface.{n}"
        )


def deserialize_query(el: Element) -> NetworkInterfaceList:
    import aws_sdk_redshift.types.network_interface

    out: NetworkInterfaceList = []
    for child in el.findall("NetworkInterface"):
        out.append(aws_sdk_redshift.types.network_interface.deserialize_query(child))
    return out


def serialize_query_flat(
    value: NetworkInterfaceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.network_interface

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.network_interface.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> NetworkInterfaceList:
    import aws_sdk_redshift.types.network_interface

    out: NetworkInterfaceList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.network_interface.deserialize_query(child))
    return out
