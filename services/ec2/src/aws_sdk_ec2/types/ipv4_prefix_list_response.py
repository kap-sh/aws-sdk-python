"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv4PrefixListResponse``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipv4_prefix_specification_response

Ipv4PrefixListResponse: TypeAlias = list[
    "aws_sdk_ec2.types.ipv4_prefix_specification_response.Ipv4PrefixSpecificationResponse"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ipv4PrefixListResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.ipv4_prefix_specification_response

        aws_sdk_ec2.types.ipv4_prefix_specification_response.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> Ipv4PrefixListResponse:
    import aws_sdk_ec2.types.ipv4_prefix_specification_response

    out: Ipv4PrefixListResponse = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.ipv4_prefix_specification_response.deserialize_ec2_query(
                child
            )
        )
    return out
