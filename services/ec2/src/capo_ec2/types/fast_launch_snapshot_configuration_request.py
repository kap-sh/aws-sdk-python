"""Generated from Smithy shape ``com.amazonaws.ec2#FastLaunchSnapshotConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer


class FastLaunchSnapshotConfigurationRequest(TypedDict, closed=True):
    target_resource_count: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of pre-provisioned snapshots to keep on hand for a Windows fast launch enabled AMI.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FastLaunchSnapshotConfigurationRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "target_resource_count" in value:
        pairs.append(
            (f"{prefix}.TargetResourceCount", str(value["target_resource_count"]))
        )


def deserialize_ec2_query(el: Element) -> FastLaunchSnapshotConfigurationRequest:
    out: FastLaunchSnapshotConfigurationRequest = {}  # type: ignore[typeddict-item]
    child_target_resource_count = el.find("TargetResourceCount")
    if child_target_resource_count is not None:
        out["target_resource_count"] = int(child_target_resource_count.text or "")
    return out
