"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateEnclaveOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class LaunchTemplateEnclaveOptions(TypedDict):
    enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If this parameter is set to <code>true</code>, the instance is enabled for Amazon Web Services Nitro Enclaves; otherwise, it is not enabled for Amazon Web Services Nitro Enclaves.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateEnclaveOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "enabled" in value:
        pairs.append((f"{prefix}.Enabled", "true" if value["enabled"] else "false"))


def deserialize_ec2_query(el: Element) -> LaunchTemplateEnclaveOptions:
    out: LaunchTemplateEnclaveOptions = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    return out
