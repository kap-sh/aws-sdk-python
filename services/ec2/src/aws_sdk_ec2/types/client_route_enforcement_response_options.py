"""Generated from Smithy shape ``com.amazonaws.ec2#ClientRouteEnforcementResponseOptions``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class ClientRouteEnforcementResponseOptions(TypedDict):
    enforced: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Status of the client route enforcement feature, indicating whether Client Route Enforcement is <code>true</code> (enabled) or <code>false</code> (disabled).</p> <p>Valid values: <code>true | false</code> </p> <p>Default value: <code>false</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientRouteEnforcementResponseOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "enforced" in value:
        pairs.append((f"{prefix}.Enforced", "true" if value["enforced"] else "false"))


def deserialize_ec2_query(el: Element) -> ClientRouteEnforcementResponseOptions:
    out: ClientRouteEnforcementResponseOptions = {}  # type: ignore[typeddict-item]
    child_enforced = el.find("Enforced")
    if child_enforced is not None:
        out["enforced"] = (child_enforced.text or "").lower() == "true"
    return out
