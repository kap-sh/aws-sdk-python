"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorPortRangeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer


class TrafficMirrorPortRangeRequest(TypedDict, closed=True):
    from_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The first port in the Traffic Mirror port range. This applies to the TCP and UDP protocols.</p>"""
    to_port: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The last port in the Traffic Mirror port range. This applies to the TCP and UDP protocols.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TrafficMirrorPortRangeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "from_port" in value:
        pairs.append((f"{prefix}.FromPort", str(value["from_port"])))
    if "to_port" in value:
        pairs.append((f"{prefix}.ToPort", str(value["to_port"])))


def deserialize_ec2_query(el: Element) -> TrafficMirrorPortRangeRequest:
    out: TrafficMirrorPortRangeRequest = {}  # type: ignore[typeddict-item]
    child_from_port = el.find("FromPort")
    if child_from_port is not None:
        out["from_port"] = int(child_from_port.text or "")
    child_to_port = el.find("ToPort")
    if child_to_port is not None:
        out["to_port"] = int(child_to_port.text or "")
    return out
