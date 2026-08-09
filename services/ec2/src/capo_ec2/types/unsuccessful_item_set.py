"""Generated from Smithy shape ``com.amazonaws.ec2#UnsuccessfulItemSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.unsuccessful_item

UnsuccessfulItemSet: TypeAlias = list[
    "capo_ec2.types.unsuccessful_item.UnsuccessfulItem"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UnsuccessfulItemSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.unsuccessful_item

        capo_ec2.types.unsuccessful_item.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> UnsuccessfulItemSet:
    import capo_ec2.types.unsuccessful_item

    out: UnsuccessfulItemSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.unsuccessful_item.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> UnsuccessfulItemSet:
    import capo_ec2.types.unsuccessful_item

    out: UnsuccessfulItemSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.unsuccessful_item.deserialize_ec2_query(child))
    return out
