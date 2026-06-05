"""Generated from Smithy shape ``com.amazonaws.ec2#ImportImageTaskList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_image_task

ImportImageTaskList: TypeAlias = list[
    "aws_sdk_ec2.types.import_image_task.ImportImageTask"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ImportImageTaskList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.import_image_task

        aws_sdk_ec2.types.import_image_task.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ImportImageTaskList:
    import aws_sdk_ec2.types.import_image_task

    out: ImportImageTaskList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.import_image_task.deserialize_ec2_query(child))
    return out
