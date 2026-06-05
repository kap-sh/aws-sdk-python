"""Generated from Smithy shape ``com.amazonaws.ec2#ByoasnSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.byoasn

ByoasnSet: TypeAlias = list["aws_sdk_ec2.types.byoasn.Byoasn"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ByoasnSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.byoasn

        aws_sdk_ec2.types.byoasn.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> ByoasnSet:
    import aws_sdk_ec2.types.byoasn

    out: ByoasnSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.byoasn.deserialize_ec2_query(child))
    return out
