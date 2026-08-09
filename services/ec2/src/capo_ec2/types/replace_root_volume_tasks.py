"""Generated from Smithy shape ``com.amazonaws.ec2#ReplaceRootVolumeTasks``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.replace_root_volume_task

ReplaceRootVolumeTasks: TypeAlias = list[
    "capo_ec2.types.replace_root_volume_task.ReplaceRootVolumeTask"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReplaceRootVolumeTasks, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.replace_root_volume_task

        capo_ec2.types.replace_root_volume_task.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ReplaceRootVolumeTasks:
    import capo_ec2.types.replace_root_volume_task

    out: ReplaceRootVolumeTasks = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.replace_root_volume_task.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ReplaceRootVolumeTasks:
    import capo_ec2.types.replace_root_volume_task

    out: ReplaceRootVolumeTasks = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.replace_root_volume_task.deserialize_ec2_query(child))
    return out
