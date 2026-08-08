"""Generated from Smithy shape ``com.amazonaws.ec2#TrafficMirrorPortRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.integer


class TrafficMirrorPortRange(TypedDict, closed=True):
    from_port: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The start of the Traffic Mirror port range. This applies to the TCP and UDP protocols.</p>"""
    to_port: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The end of the Traffic Mirror port range. This applies to the TCP and UDP protocols.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: TrafficMirrorPortRange, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "from_port" in value:
        pairs.append((f"{key_prefix}FromPort", str(value["from_port"])))
    if "to_port" in value:
        pairs.append((f"{key_prefix}ToPort", str(value["to_port"])))


def deserialize_ec2_query(el: Element) -> TrafficMirrorPortRange:
    out: TrafficMirrorPortRange = {}  # type: ignore[typeddict-item]
    child_from_port = el.find("fromPort")
    if child_from_port is not None:
        out["from_port"] = int(child_from_port.text or "")
    child_to_port = el.find("toPort")
    if child_to_port is not None:
        out["to_port"] = int(child_to_port.text or "")
    return out
