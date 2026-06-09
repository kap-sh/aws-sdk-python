"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateDnsDetailsSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.private_dns_details

PrivateDnsDetailsSet: TypeAlias = list[
    "aws_sdk_ec2.types.private_dns_details.PrivateDnsDetails"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrivateDnsDetailsSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.private_dns_details

        aws_sdk_ec2.types.private_dns_details.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> PrivateDnsDetailsSet:
    import aws_sdk_ec2.types.private_dns_details

    out: PrivateDnsDetailsSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.private_dns_details.deserialize_ec2_query(child))
    return out
