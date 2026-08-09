"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceGenerationSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_generation

InstanceGenerationSet: TypeAlias = list[
    "capo_ec2.types.instance_generation.InstanceGeneration"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceGenerationSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.instance_generation

        capo_ec2.types.instance_generation.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> InstanceGenerationSet:
    import capo_ec2.types.instance_generation

    out: InstanceGenerationSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.instance_generation.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> InstanceGenerationSet:
    import capo_ec2.types.instance_generation

    out: InstanceGenerationSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.instance_generation.deserialize_ec2_query(child))
    return out
