"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyTrafficMirrorSessionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.traffic_mirror_session


class ModifyTrafficMirrorSessionResult(TypedDict, closed=True):
    traffic_mirror_session: NotRequired[
        "capo_ec2.types.traffic_mirror_session.TrafficMirrorSession"
    ]
    """<p>Information about the Traffic Mirror session.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyTrafficMirrorSessionResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "traffic_mirror_session" in value:
        import capo_ec2.types.traffic_mirror_session

        capo_ec2.types.traffic_mirror_session.serialize_ec2_query(
            value["traffic_mirror_session"], pairs, f"{key_prefix}TrafficMirrorSession"
        )


def deserialize_ec2_query(el: Element) -> ModifyTrafficMirrorSessionResult:
    out: ModifyTrafficMirrorSessionResult = {}  # type: ignore[typeddict-item]
    child_traffic_mirror_session = el.find("trafficMirrorSession")
    if child_traffic_mirror_session is not None:
        import capo_ec2.types.traffic_mirror_session

        out["traffic_mirror_session"] = (
            capo_ec2.types.traffic_mirror_session.deserialize_ec2_query(
                child_traffic_mirror_session
            )
        )
    return out
