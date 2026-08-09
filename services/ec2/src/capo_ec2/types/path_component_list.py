"""Generated from Smithy shape ``com.amazonaws.ec2#PathComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.path_component

PathComponentList: TypeAlias = list["capo_ec2.types.path_component.PathComponent"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PathComponentList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.path_component

        capo_ec2.types.path_component.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> PathComponentList:
    import capo_ec2.types.path_component

    out: PathComponentList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.path_component.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> PathComponentList:
    import capo_ec2.types.path_component

    out: PathComponentList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.path_component.deserialize_ec2_query(child))
    return out
