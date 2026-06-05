"""Generated from Smithy shape ``com.amazonaws.ec2#IpamScopeSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_scope

IpamScopeSet: TypeAlias = list["aws_sdk_ec2.types.ipam_scope.IpamScope"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamScopeSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.ipam_scope

        aws_sdk_ec2.types.ipam_scope.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> IpamScopeSet:
    import aws_sdk_ec2.types.ipam_scope

    out: IpamScopeSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.ipam_scope.deserialize_ec2_query(child))
    return out
