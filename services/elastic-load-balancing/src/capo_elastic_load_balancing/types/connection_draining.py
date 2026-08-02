"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#ConnectionDraining``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.connection_draining_enabled
    import capo_elastic_load_balancing.types.connection_draining_timeout


class ConnectionDraining(TypedDict, closed=True):
    enabled: "capo_elastic_load_balancing.types.connection_draining_enabled.ConnectionDrainingEnabled"
    """<p>Specifies whether connection draining is enabled for the load balancer.</p>"""
    timeout: NotRequired[
        "capo_elastic_load_balancing.types.connection_draining_timeout.ConnectionDrainingTimeout"
    ]
    """<p>The maximum time, in seconds, to keep the existing connections open before deregistering the instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ConnectionDraining, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append(
        (f"{key_prefix}Enabled", "true" if value.get("enabled", False) else "false")
    )
    if "timeout" in value:
        pairs.append((f"{key_prefix}Timeout", str(value["timeout"])))


def deserialize_query(el: Element) -> ConnectionDraining:
    out: ConnectionDraining = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    else:
        out["enabled"] = False
    child_timeout = el.find("Timeout")
    if child_timeout is not None:
        out["timeout"] = int(child_timeout.text or "")
    return out
