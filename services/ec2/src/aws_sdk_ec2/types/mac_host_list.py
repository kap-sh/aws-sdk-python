"""Generated from Smithy shape ``com.amazonaws.ec2#MacHostList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.mac_host

MacHostList: TypeAlias = list["aws_sdk_ec2.types.mac_host.MacHost"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MacHostList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.mac_host

        aws_sdk_ec2.types.mac_host.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> MacHostList:
    import aws_sdk_ec2.types.mac_host

    out: MacHostList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.mac_host.deserialize_ec2_query(child))
    return out
