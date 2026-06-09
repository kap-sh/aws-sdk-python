"""Generated from Smithy shape ``com.amazonaws.ec2#LocalGatewaySet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.local_gateway

LocalGatewaySet: TypeAlias = list["aws_sdk_ec2.types.local_gateway.LocalGateway"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LocalGatewaySet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.local_gateway

        aws_sdk_ec2.types.local_gateway.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> LocalGatewaySet:
    import aws_sdk_ec2.types.local_gateway

    out: LocalGatewaySet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.local_gateway.deserialize_ec2_query(child))
    return out
