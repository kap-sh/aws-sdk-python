"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTrafficMirrorFilterResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class DeleteTrafficMirrorFilterResult(TypedDict, closed=True):
    traffic_mirror_filter_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Traffic Mirror filter.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTrafficMirrorFilterResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "traffic_mirror_filter_id" in value:
        pairs.append(
            (f"{prefix}.TrafficMirrorFilterId", str(value["traffic_mirror_filter_id"]))
        )


def deserialize_ec2_query(el: Element) -> DeleteTrafficMirrorFilterResult:
    out: DeleteTrafficMirrorFilterResult = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_filter_id = el.find("TrafficMirrorFilterId")
    if child_traffic_mirror_filter_id is not None:
        out["traffic_mirror_filter_id"] = str(child_traffic_mirror_filter_id.text or "")
    return out
