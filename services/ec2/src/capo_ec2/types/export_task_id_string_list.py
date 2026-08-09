"""Generated from Smithy shape ``com.amazonaws.ec2#ExportTaskIdStringList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.export_task_id

ExportTaskIdStringList: TypeAlias = list["capo_ec2.types.export_task_id.ExportTaskId"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportTaskIdStringList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_ec2_query(el: Element) -> ExportTaskIdStringList:
    out: ExportTaskIdStringList = []
    for child in el.findall("ExportTaskId"):
        out.append(str(child.text or ""))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ExportTaskIdStringList:
    out: ExportTaskIdStringList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
