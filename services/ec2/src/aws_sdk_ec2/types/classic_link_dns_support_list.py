"""Generated from Smithy shape ``com.amazonaws.ec2#ClassicLinkDnsSupportList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.classic_link_dns_support

ClassicLinkDnsSupportList: TypeAlias = list[
    "aws_sdk_ec2.types.classic_link_dns_support.ClassicLinkDnsSupport"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClassicLinkDnsSupportList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.classic_link_dns_support

        aws_sdk_ec2.types.classic_link_dns_support.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ClassicLinkDnsSupportList:
    import aws_sdk_ec2.types.classic_link_dns_support

    out: ClassicLinkDnsSupportList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.classic_link_dns_support.deserialize_ec2_query(child)
        )
    return out
