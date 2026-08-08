"""Generated from Smithy shape ``com.amazonaws.ec2#ClassicLoadBalancer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class ClassicLoadBalancer(TypedDict, closed=True):
    name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name of the load balancer.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClassicLoadBalancer, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))


def deserialize_ec2_query(el: Element) -> ClassicLoadBalancer:
    out: ClassicLoadBalancer = {}  # type: ignore[typeddict-item]
    child_name = el.find("name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    return out
