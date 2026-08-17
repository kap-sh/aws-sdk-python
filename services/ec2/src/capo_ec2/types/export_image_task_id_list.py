"""Generated from Smithy shape ``com.amazonaws.ec2#ExportImageTaskIdList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.export_image_task_id

ExportImageTaskIdList: TypeAlias = list[
    "capo_ec2.types.export_image_task_id.ExportImageTaskId"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportImageTaskIdList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(el: Element) -> ExportImageTaskIdList:
    out: ExportImageTaskIdList = []
    for child in el.findall("ExportImageTaskId"):
        out.append(str(child.text or ""))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ExportImageTaskIdList:
    out: ExportImageTaskIdList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
