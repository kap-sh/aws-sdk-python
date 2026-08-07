"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#Limit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.max
    import capo_elastic_load_balancing_v2.types.name


class Limit(TypedDict, closed=True):
    name: NotRequired["capo_elastic_load_balancing_v2.types.name.Name"]
    """<p>The name of the limit.</p>"""
    max: NotRequired["capo_elastic_load_balancing_v2.types.max.Max"]
    """<p>The maximum value of the limit.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Limit, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "max" in value:
        pairs.append((f"{key_prefix}Max", str(value["max"])))


def deserialize_query(el: Element) -> Limit:
    out: Limit = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_max = el.find("Max")
    if child_max is not None:
        out["max"] = str(child_max.text or "")
    return out
