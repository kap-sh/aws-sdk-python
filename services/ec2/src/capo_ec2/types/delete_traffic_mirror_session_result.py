"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTrafficMirrorSessionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class DeleteTrafficMirrorSessionResult(TypedDict, closed=True):
    traffic_mirror_session_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the deleted Traffic Mirror session.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTrafficMirrorSessionResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "traffic_mirror_session_id" in value:
        pairs.append(
            (
                f"{key_prefix}TrafficMirrorSessionId",
                str(value["traffic_mirror_session_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> DeleteTrafficMirrorSessionResult:
    out: DeleteTrafficMirrorSessionResult = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_session_id = el.find("TrafficMirrorSessionId")
    if child_traffic_mirror_session_id is not None:
        out["traffic_mirror_session_id"] = str(
            child_traffic_mirror_session_id.text or ""
        )
    return out
