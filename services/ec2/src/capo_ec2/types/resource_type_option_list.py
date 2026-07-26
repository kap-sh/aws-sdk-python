"""Generated from Smithy shape ``com.amazonaws.ec2#ResourceTypeOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.resource_type_option

ResourceTypeOptionList: TypeAlias = list[
    "capo_ec2.types.resource_type_option.ResourceTypeOption"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ResourceTypeOptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.resource_type_option

        capo_ec2.types.resource_type_option.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ResourceTypeOptionList:
    import capo_ec2.types.resource_type_option

    out: ResourceTypeOptionList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.resource_type_option.deserialize_ec2_query(child))
    return out
