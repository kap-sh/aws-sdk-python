"""Generated from Smithy shape ``com.amazonaws.ec2#BandwidthWeightingTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.bandwidth_weighting_type

BandwidthWeightingTypeList: TypeAlias = list[
    "capo_ec2.types.bandwidth_weighting_type.BandwidthWeightingType"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: BandwidthWeightingTypeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.bandwidth_weighting_type

        capo_ec2.types.bandwidth_weighting_type.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> BandwidthWeightingTypeList:
    import capo_ec2.types.bandwidth_weighting_type

    out: BandwidthWeightingTypeList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.bandwidth_weighting_type.deserialize_ec2_query(child))
    return out
