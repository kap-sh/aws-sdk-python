"""Generated from Smithy shape ``com.amazonaws.ec2#SecondaryInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.secondary_interface

SecondaryInterfaceList: TypeAlias = list[
    "capo_ec2.types.secondary_interface.SecondaryInterface"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SecondaryInterfaceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.secondary_interface

        capo_ec2.types.secondary_interface.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> SecondaryInterfaceList:
    import capo_ec2.types.secondary_interface

    out: SecondaryInterfaceList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.secondary_interface.deserialize_ec2_query(child))
    return out
