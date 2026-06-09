"""Generated from Smithy shape ``com.amazonaws.ec2#VpcEndpointSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpc_endpoint

VpcEndpointSet: TypeAlias = list["aws_sdk_ec2.types.vpc_endpoint.VpcEndpoint"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcEndpointSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.vpc_endpoint

        aws_sdk_ec2.types.vpc_endpoint.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> VpcEndpointSet:
    import aws_sdk_ec2.types.vpc_endpoint

    out: VpcEndpointSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.vpc_endpoint.deserialize_ec2_query(child))
    return out
