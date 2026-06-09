"""Generated from Smithy shape ``com.amazonaws.ec2#FilterList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.filter

FilterList: TypeAlias = list["aws_sdk_ec2.types.filter.Filter"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FilterList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.filter

        aws_sdk_ec2.types.filter.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> FilterList:
    import aws_sdk_ec2.types.filter

    out: FilterList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.filter.deserialize_ec2_query(child))
    return out
