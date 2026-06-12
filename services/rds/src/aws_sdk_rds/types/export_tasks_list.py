"""Generated from Smithy shape ``com.amazonaws.rds#ExportTasksList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.export_task

ExportTasksList: TypeAlias = list["aws_sdk_rds.types.export_task.ExportTask"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ExportTasksList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.export_task

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.export_task.serialize_query(
            item, pairs, f"{prefix}.ExportTask.{n}"
        )


def deserialize_query(el: Element) -> ExportTasksList:
    import aws_sdk_rds.types.export_task

    out: ExportTasksList = []
    for child in el.findall("ExportTask"):
        out.append(aws_sdk_rds.types.export_task.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ExportTasksList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.export_task

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.export_task.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ExportTasksList:
    import aws_sdk_rds.types.export_task

    out: ExportTasksList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.export_task.deserialize_query(child))
    return out
