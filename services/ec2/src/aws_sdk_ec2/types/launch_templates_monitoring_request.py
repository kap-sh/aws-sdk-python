"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplatesMonitoringRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class LaunchTemplatesMonitoringRequest(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specify <code>true</code> to enable detailed monitoring. Otherwise, basic monitoring is enabled.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplatesMonitoringRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "enabled" in value:
        pairs.append((f"{prefix}.Enabled", "true" if value["enabled"] else "false"))


def deserialize_ec2_query(el: Element) -> LaunchTemplatesMonitoringRequest:
    out: LaunchTemplatesMonitoringRequest = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    return out
