"""Generated from Smithy shape ``com.amazonaws.rds#CancelExportTaskMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class CancelExportTaskMessage(TypedDict):
    export_task_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The identifier of the snapshot or cluster export task to cancel.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CancelExportTaskMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "export_task_identifier" in value:
        pairs.append(
            (f"{prefix}.ExportTaskIdentifier", str(value["export_task_identifier"]))
        )


def deserialize_query(el: Element) -> CancelExportTaskMessage:
    out: CancelExportTaskMessage = {}  # type: ignore[typeddict-item]
    child_export_task_identifier = el.find("ExportTaskIdentifier")
    if child_export_task_identifier is not None:
        out["export_task_identifier"] = str(child_export_task_identifier.text or "")
    return out
