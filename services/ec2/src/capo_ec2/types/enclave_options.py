"""Generated from Smithy shape ``com.amazonaws.ec2#EnclaveOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class EnclaveOptions(TypedDict, closed=True):
    enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If this parameter is set to <code>true</code>, the instance is enabled for Amazon Web Services Nitro Enclaves; otherwise, it is not enabled for Amazon Web Services Nitro Enclaves.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: EnclaveOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "enabled" in value:
        pairs.append((f"{key_prefix}Enabled", "true" if value["enabled"] else "false"))


def deserialize_ec2_query(el: Element) -> EnclaveOptions:
    out: EnclaveOptions = {}  # type: ignore[typeddict-item]
    child_enabled = el.find("Enabled")
    if child_enabled is not None:
        out["enabled"] = (child_enabled.text or "").lower() == "true"
    return out
