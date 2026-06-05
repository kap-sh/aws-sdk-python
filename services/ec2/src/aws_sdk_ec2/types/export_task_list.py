"""Generated from Smithy shape ``com.amazonaws.ec2#ExportTaskList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_task

ExportTaskList: TypeAlias = list["aws_sdk_ec2.types.export_task.ExportTask"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportTaskList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.export_task

        aws_sdk_ec2.types.export_task.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> ExportTaskList:
    import aws_sdk_ec2.types.export_task

    out: ExportTaskList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.export_task.deserialize_ec2_query(child))
    return out
