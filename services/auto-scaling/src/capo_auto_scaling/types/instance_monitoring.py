"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceMonitoring``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.monitoring_enabled


class InstanceMonitoring(TypedDict, closed=True):
    enabled: NotRequired["capo_auto_scaling.types.monitoring_enabled.MonitoringEnabled"]
    """<p>If <code>true</code>, detailed monitoring is enabled. Otherwise, basic monitoring is enabled.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceMonitoring, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "enabled" in value:
        pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))


def deserialize_query(el: Element) -> InstanceMonitoring:
    out: InstanceMonitoring = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    return out
