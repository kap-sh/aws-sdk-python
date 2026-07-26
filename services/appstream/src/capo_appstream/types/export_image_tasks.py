"""Generated from Smithy shape ``com.amazonaws.appstream#ExportImageTasks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.export_image_task

ExportImageTasks: TypeAlias = list[
    "capo_appstream.types.export_image_task.ExportImageTask"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportImageTasks) -> list:
    import capo_appstream.types.export_image_task

    out: list = []
    for item in value:
        out.append(capo_appstream.types.export_image_task.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExportImageTasks:
    import capo_appstream.types.export_image_task

    out: ExportImageTasks = []
    for item in data:
        out.append(
            capo_appstream.types.export_image_task.deserialize_aws_json_1_1(item)
        )
    return out
