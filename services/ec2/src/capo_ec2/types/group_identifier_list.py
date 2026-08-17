"""Generated from Smithy shape ``com.amazonaws.ec2#GroupIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.group_identifier

GroupIdentifierList: TypeAlias = list["capo_ec2.types.group_identifier.GroupIdentifier"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GroupIdentifierList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.group_identifier

        capo_ec2.types.group_identifier.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> GroupIdentifierList:
    import capo_ec2.types.group_identifier

    out: GroupIdentifierList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.group_identifier.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> GroupIdentifierList:
    import capo_ec2.types.group_identifier

    out: GroupIdentifierList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.group_identifier.deserialize_ec2_query(child))
    return out
