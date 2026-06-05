"""Generated from Smithy shape ``com.amazonaws.ec2#PropagatingVgw``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class PropagatingVgw(TypedDict):
    gateway_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the virtual private gateway.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PropagatingVgw, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "gateway_id" in value:
        pairs.append((f"{prefix}.GatewayId", str(value["gateway_id"])))


def deserialize_ec2_query(el: Element) -> PropagatingVgw:
    out: PropagatingVgw = {}  # type: ignore[typeddict-item]
    child_gateway_id = el.find("GatewayId")
    if child_gateway_id is not None:
        out["gateway_id"] = str(child_gateway_id.text or "")
    return out
