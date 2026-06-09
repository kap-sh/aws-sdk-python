"""Generated from Smithy shape ``com.amazonaws.ec2#CreateReplaceRootVolumeTaskResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.replace_root_volume_task


class CreateReplaceRootVolumeTaskResult(TypedDict):
    replace_root_volume_task: NotRequired[
        "aws_sdk_ec2.types.replace_root_volume_task.ReplaceRootVolumeTask"
    ]
    """<p>Information about the root volume replacement task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateReplaceRootVolumeTaskResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "replace_root_volume_task" in value:
        import aws_sdk_ec2.types.replace_root_volume_task

        aws_sdk_ec2.types.replace_root_volume_task.serialize_ec2_query(
            value["replace_root_volume_task"], pairs, f"{prefix}.ReplaceRootVolumeTask"
        )


def deserialize_ec2_query(el: Element) -> CreateReplaceRootVolumeTaskResult:
    out: CreateReplaceRootVolumeTaskResult = {}  # type: ignore[typeddict-item]
    child_replace_root_volume_task = el.find("ReplaceRootVolumeTask")
    if child_replace_root_volume_task is not None:
        import aws_sdk_ec2.types.replace_root_volume_task

        out["replace_root_volume_task"] = (
            aws_sdk_ec2.types.replace_root_volume_task.deserialize_ec2_query(
                child_replace_root_volume_task
            )
        )
    return out
