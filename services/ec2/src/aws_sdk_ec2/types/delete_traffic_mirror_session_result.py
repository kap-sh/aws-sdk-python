"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTrafficMirrorSessionResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class DeleteTrafficMirrorSessionResult(TypedDict):
    traffic_mirror_session_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the deleted Traffic Mirror session.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTrafficMirrorSessionResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "traffic_mirror_session_id" in value:
        pairs.append(
            (
                f"{prefix}.TrafficMirrorSessionId",
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
