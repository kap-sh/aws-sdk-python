"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateHibernationOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class LaunchTemplateHibernationOptionsRequest(TypedDict):
    configured: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If you set this parameter to <code>true</code>, the instance is enabled for hibernation.</p> <p>Default: <code>false</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateHibernationOptionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "configured" in value:
        pairs.append(
            (f"{prefix}.Configured", "true" if value["configured"] else "false")
        )


def deserialize_ec2_query(el: Element) -> LaunchTemplateHibernationOptionsRequest:
    out: LaunchTemplateHibernationOptionsRequest = {}  # type: ignore[typeddict-item]
    child_configured = el.find("Configured")
    if child_configured is not None:
        out["configured"] = (child_configured.text or "").lower() == "true"
    return out
