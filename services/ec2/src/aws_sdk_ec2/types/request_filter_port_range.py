"""Generated from Smithy shape ``com.amazonaws.ec2#RequestFilterPortRange``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.port


class RequestFilterPortRange(TypedDict):
    from_port: NotRequired["aws_sdk_ec2.types.port.Port"]
    """<p>The first port in the range.</p>"""
    to_port: NotRequired["aws_sdk_ec2.types.port.Port"]
    """<p>The last port in the range.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RequestFilterPortRange, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "from_port" in value:
        pairs.append((f"{prefix}.FromPort", str(value["from_port"])))
    if "to_port" in value:
        pairs.append((f"{prefix}.ToPort", str(value["to_port"])))


def deserialize_ec2_query(el: Element) -> RequestFilterPortRange:
    out: RequestFilterPortRange = {}  # type: ignore[typeddict-item]
    child_from_port = el.find("FromPort")
    if child_from_port is not None:
        out["from_port"] = int(child_from_port.text or "")
    child_to_port = el.find("ToPort")
    if child_to_port is not None:
        out["to_port"] = int(child_to_port.text or "")
    return out
