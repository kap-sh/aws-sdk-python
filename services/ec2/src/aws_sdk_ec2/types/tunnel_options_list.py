"""Generated from Smithy shape ``com.amazonaws.ec2#TunnelOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.tunnel_option

TunnelOptionsList: TypeAlias = list["aws_sdk_ec2.types.tunnel_option.TunnelOption"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TunnelOptionsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.tunnel_option

        aws_sdk_ec2.types.tunnel_option.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> TunnelOptionsList:
    import aws_sdk_ec2.types.tunnel_option

    out: TunnelOptionsList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.tunnel_option.deserialize_ec2_query(child))
    return out
