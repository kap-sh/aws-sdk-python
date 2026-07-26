"""Generated from Smithy shape ``com.amazonaws.redshift#NetworkInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.network_interface

NetworkInterfaceList: TypeAlias = list[
    "capo_redshift.types.network_interface.NetworkInterface"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: NetworkInterfaceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.network_interface

    for n, item in enumerate(value, 1):
        capo_redshift.types.network_interface.serialize_query(
            item, pairs, f"{prefix}.NetworkInterface.{n}"
        )


def deserialize_query(el: Element) -> NetworkInterfaceList:
    import capo_redshift.types.network_interface

    out: NetworkInterfaceList = []
    for child in el.findall("NetworkInterface"):
        out.append(capo_redshift.types.network_interface.deserialize_query(child))
    return out


def serialize_query_flat(
    value: NetworkInterfaceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_redshift.types.network_interface

    for n, item in enumerate(value, 1):
        capo_redshift.types.network_interface.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> NetworkInterfaceList:
    import capo_redshift.types.network_interface

    out: NetworkInterfaceList = []
    for child in parent.findall(tag):
        out.append(capo_redshift.types.network_interface.deserialize_query(child))
    return out
