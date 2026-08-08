"""Generated from Smithy shape ``com.amazonaws.ec2#RunInstancesMonitoringEnabled``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class RunInstancesMonitoringEnabled(TypedDict, closed=True):
    enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether detailed monitoring is enabled. Otherwise, basic monitoring is enabled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RunInstancesMonitoringEnabled, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "enabled" in value:
        pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))


def deserialize_ec2_query(el: Element) -> RunInstancesMonitoringEnabled:
    out: RunInstancesMonitoringEnabled = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    return out
