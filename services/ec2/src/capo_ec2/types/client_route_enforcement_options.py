"""Generated from Smithy shape ``com.amazonaws.ec2#ClientRouteEnforcementOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class ClientRouteEnforcementOptions(TypedDict, closed=True):
    enforced: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Enable or disable Client Route Enforcement. The state can either be <code>true</code> (enabled) or <code>false</code> (disabled). The default is <code>false</code>.</p> <p>Valid values: <code>true | false</code> </p> <p>Default value: <code>false</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientRouteEnforcementOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "enforced" in value:
        pairs.append((f"{prefix}.Enforced", "true" if value["enforced"] else "false"))


def deserialize_ec2_query(el: Element) -> ClientRouteEnforcementOptions:
    out: ClientRouteEnforcementOptions = {}  # type: ignore[typeddict-item]
    child_enforced = el.find("Enforced")
    if child_enforced is not None:
        out["enforced"] = (child_enforced.text or "").lower() == "true"
    return out
