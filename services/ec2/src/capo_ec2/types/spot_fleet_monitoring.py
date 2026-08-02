"""Generated from Smithy shape ``com.amazonaws.ec2#SpotFleetMonitoring``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class SpotFleetMonitoring(TypedDict, closed=True):
    enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Enables monitoring for the instance.</p> <p>Default: <code>false</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotFleetMonitoring, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "enabled" in value:
        pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))


def deserialize_ec2_query(el: Element) -> SpotFleetMonitoring:
    out: SpotFleetMonitoring = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    return out
