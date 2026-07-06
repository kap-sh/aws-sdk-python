"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceRefreshWarmPoolProgress``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.instances_to_update
    import aws_sdk_auto_scaling.types.int_percent


class InstanceRefreshWarmPoolProgress(TypedDict, closed=True):
    percentage_complete: NotRequired[
        "aws_sdk_auto_scaling.types.int_percent.IntPercent"
    ]
    """<p>The percentage of instances in the warm pool that have been replaced. For each instance replacement, Amazon EC2 Auto Scaling tracks the instance's health status and warm-up time. When the instance's health status changes to healthy and the specified warm-up time passes, the instance is considered updated and is added to the percentage complete.</p>"""
    instances_to_update: NotRequired[
        "aws_sdk_auto_scaling.types.instances_to_update.InstancesToUpdate"
    ]
    """<p>The number of instances remaining to update.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceRefreshWarmPoolProgress, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "percentage_complete" in value:
        pairs.append(
            (f"{prefix}.PercentageComplete", str(value["percentage_complete"]))
        )
    if "instances_to_update" in value:
        pairs.append((f"{prefix}.InstancesToUpdate", str(value["instances_to_update"])))


def deserialize_query(el: Element) -> InstanceRefreshWarmPoolProgress:
    out: InstanceRefreshWarmPoolProgress = {}  # type: ignore[typeddict-item]
    child_percentage_complete = el.find("PercentageComplete")
    if child_percentage_complete is not None:
        out["percentage_complete"] = int(child_percentage_complete.text or "")
    child_instances_to_update = el.find("InstancesToUpdate")
    if child_instances_to_update is not None:
        out["instances_to_update"] = int(child_instances_to_update.text or "")
    return out
