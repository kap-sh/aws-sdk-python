"""Generated from Smithy shape ``com.amazonaws.ec2#TargetNetworkSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.target_network

TargetNetworkSet: TypeAlias = list["aws_sdk_ec2.types.target_network.TargetNetwork"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TargetNetworkSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.target_network

        aws_sdk_ec2.types.target_network.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> TargetNetworkSet:
    import aws_sdk_ec2.types.target_network

    out: TargetNetworkSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.target_network.deserialize_ec2_query(child))
    return out
