"""Generated from Smithy shape ``com.amazonaws.ec2#PropagatingVgwList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.propagating_vgw

PropagatingVgwList: TypeAlias = list["aws_sdk_ec2.types.propagating_vgw.PropagatingVgw"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PropagatingVgwList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.propagating_vgw

        aws_sdk_ec2.types.propagating_vgw.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> PropagatingVgwList:
    import aws_sdk_ec2.types.propagating_vgw

    out: PropagatingVgwList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.propagating_vgw.deserialize_ec2_query(child))
    return out
