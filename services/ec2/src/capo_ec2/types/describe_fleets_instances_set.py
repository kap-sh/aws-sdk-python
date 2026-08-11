"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleetsInstancesSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.describe_fleets_instances

DescribeFleetsInstancesSet: TypeAlias = list[
    "capo_ec2.types.describe_fleets_instances.DescribeFleetsInstances"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFleetsInstancesSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.describe_fleets_instances

        capo_ec2.types.describe_fleets_instances.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> DescribeFleetsInstancesSet:
    import capo_ec2.types.describe_fleets_instances

    out: DescribeFleetsInstancesSet = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.describe_fleets_instances.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> DescribeFleetsInstancesSet:
    import capo_ec2.types.describe_fleets_instances

    out: DescribeFleetsInstancesSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.describe_fleets_instances.deserialize_ec2_query(child)
        )
    return out
