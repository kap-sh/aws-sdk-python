"""Generated from Smithy shape ``com.amazonaws.ec2#SupportedRegionSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.supported_region_detail

SupportedRegionSet: TypeAlias = list[
    "capo_ec2.types.supported_region_detail.SupportedRegionDetail"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SupportedRegionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.supported_region_detail

        capo_ec2.types.supported_region_detail.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> SupportedRegionSet:
    import capo_ec2.types.supported_region_detail

    out: SupportedRegionSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.supported_region_detail.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> SupportedRegionSet:
    import capo_ec2.types.supported_region_detail

    out: SupportedRegionSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.supported_region_detail.deserialize_ec2_query(child))
    return out
