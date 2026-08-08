"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateHibernationOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class LaunchTemplateHibernationOptions(TypedDict, closed=True):
    configured: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If this parameter is set to <code>true</code>, the instance is enabled for hibernation; otherwise, it is not enabled for hibernation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateHibernationOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "configured" in value:
        pairs.append(
            (f"{key_prefix}Configured", "true" if value["configured"] else "false")
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateHibernationOptions:
    out: LaunchTemplateHibernationOptions = {}  # type: ignore[typeddict-item]
    child_configured = el.find("configured")
    if child_configured is not None:
        out["configured"] = (child_configured.text or "").lower() == "true"
    return out
