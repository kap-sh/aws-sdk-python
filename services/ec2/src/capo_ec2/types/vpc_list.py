"""Generated from Smithy shape ``com.amazonaws.ec2#VpcList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.vpc

VpcList: TypeAlias = list["capo_ec2.types.vpc.Vpc"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpcList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.vpc

        capo_ec2.types.vpc.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> VpcList:
    import capo_ec2.types.vpc

    out: VpcList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.vpc.deserialize_ec2_query(child))
    return out
