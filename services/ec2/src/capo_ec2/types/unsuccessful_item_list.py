"""Generated from Smithy shape ``com.amazonaws.ec2#UnsuccessfulItemList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.unsuccessful_item

UnsuccessfulItemList: TypeAlias = list[
    "capo_ec2.types.unsuccessful_item.UnsuccessfulItem"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UnsuccessfulItemList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.unsuccessful_item

        capo_ec2.types.unsuccessful_item.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> UnsuccessfulItemList:
    import capo_ec2.types.unsuccessful_item

    out: UnsuccessfulItemList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.unsuccessful_item.deserialize_ec2_query(child))
    return out
