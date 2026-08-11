"""Generated from Smithy shape ``com.amazonaws.ec2#MacModificationTaskList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.mac_modification_task

MacModificationTaskList: TypeAlias = list[
    "capo_ec2.types.mac_modification_task.MacModificationTask"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MacModificationTaskList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.mac_modification_task

        capo_ec2.types.mac_modification_task.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> MacModificationTaskList:
    import capo_ec2.types.mac_modification_task

    out: MacModificationTaskList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.mac_modification_task.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> MacModificationTaskList:
    import capo_ec2.types.mac_modification_task

    out: MacModificationTaskList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.mac_modification_task.deserialize_ec2_query(child))
    return out
