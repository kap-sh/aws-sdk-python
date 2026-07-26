"""Generated from Smithy shape ``com.amazonaws.ec2#ServiceDetailSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.service_detail

ServiceDetailSet: TypeAlias = list["capo_ec2.types.service_detail.ServiceDetail"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ServiceDetailSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.service_detail

        capo_ec2.types.service_detail.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> ServiceDetailSet:
    import capo_ec2.types.service_detail

    out: ServiceDetailSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.service_detail.deserialize_ec2_query(child))
    return out
