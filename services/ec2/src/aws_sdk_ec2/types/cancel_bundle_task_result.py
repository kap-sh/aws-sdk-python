"""Generated from Smithy shape ``com.amazonaws.ec2#CancelBundleTaskResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.bundle_task


class CancelBundleTaskResult(TypedDict):
    bundle_task: NotRequired["aws_sdk_ec2.types.bundle_task.BundleTask"]
    """<p>Information about the bundle task.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelBundleTaskResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "bundle_task" in value:
        import aws_sdk_ec2.types.bundle_task

        aws_sdk_ec2.types.bundle_task.serialize_ec2_query(
            value["bundle_task"], pairs, f"{prefix}.BundleInstanceTask"
        )


def deserialize_ec2_query(el: Element) -> CancelBundleTaskResult:
    out: CancelBundleTaskResult = {}  # type: ignore[typeddict-item]
    child_bundle_task = el.find("BundleInstanceTask")
    if child_bundle_task is not None:
        import aws_sdk_ec2.types.bundle_task

        out["bundle_task"] = aws_sdk_ec2.types.bundle_task.deserialize_ec2_query(
            child_bundle_task
        )
    return out
