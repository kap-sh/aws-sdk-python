"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTrafficMirrorTargetResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class DeleteTrafficMirrorTargetResult(TypedDict, closed=True):
    traffic_mirror_target_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the deleted Traffic Mirror target.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTrafficMirrorTargetResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "traffic_mirror_target_id" in value:
        pairs.append(
            (
                f"{key_prefix}TrafficMirrorTargetId",
                str(value["traffic_mirror_target_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> DeleteTrafficMirrorTargetResult:
    out: DeleteTrafficMirrorTargetResult = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_target_id = el.find("TrafficMirrorTargetId")
    if child_traffic_mirror_target_id is not None:
        out["traffic_mirror_target_id"] = str(child_traffic_mirror_target_id.text or "")
    return out
