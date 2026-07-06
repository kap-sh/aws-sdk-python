"""Generated from Smithy shape ``com.amazonaws.ec2#CreateDelegateMacVolumeOwnershipTaskResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.mac_modification_task


class CreateDelegateMacVolumeOwnershipTaskResult(TypedDict, closed=True):
    mac_modification_task: NotRequired[
        "aws_sdk_ec2.types.mac_modification_task.MacModificationTask"
    ]
    """<p>Information about the volume ownership delegation task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateDelegateMacVolumeOwnershipTaskResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "mac_modification_task" in value:
        import aws_sdk_ec2.types.mac_modification_task

        aws_sdk_ec2.types.mac_modification_task.serialize_ec2_query(
            value["mac_modification_task"], pairs, f"{prefix}.MacModificationTask"
        )


def deserialize_ec2_query(el: Element) -> CreateDelegateMacVolumeOwnershipTaskResult:
    out: CreateDelegateMacVolumeOwnershipTaskResult = {}  # type: ignore[typeddict-item]
    child_mac_modification_task = el.find("MacModificationTask")
    if child_mac_modification_task is not None:
        import aws_sdk_ec2.types.mac_modification_task

        out["mac_modification_task"] = (
            aws_sdk_ec2.types.mac_modification_task.deserialize_ec2_query(
                child_mac_modification_task
            )
        )
    return out
