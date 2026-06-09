"""Generated from Smithy shape ``com.amazonaws.ec2#TagList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.tag

TagList: TypeAlias = list["aws_sdk_ec2.types.tag.Tag"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TagList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.tag

        aws_sdk_ec2.types.tag.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> TagList:
    import aws_sdk_ec2.types.tag

    out: TagList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.tag.deserialize_ec2_query(child))
    return out
