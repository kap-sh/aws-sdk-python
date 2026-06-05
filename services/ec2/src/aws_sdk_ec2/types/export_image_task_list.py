"""Generated from Smithy shape ``com.amazonaws.ec2#ExportImageTaskList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.export_image_task

ExportImageTaskList: TypeAlias = list[
    "aws_sdk_ec2.types.export_image_task.ExportImageTask"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ExportImageTaskList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.export_image_task

        aws_sdk_ec2.types.export_image_task.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ExportImageTaskList:
    import aws_sdk_ec2.types.export_image_task

    out: ExportImageTaskList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.export_image_task.deserialize_ec2_query(child))
    return out
