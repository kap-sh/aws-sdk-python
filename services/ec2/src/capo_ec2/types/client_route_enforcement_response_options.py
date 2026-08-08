"""Generated from Smithy shape ``com.amazonaws.ec2#ClientRouteEnforcementResponseOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class ClientRouteEnforcementResponseOptions(TypedDict, closed=True):
    enforced: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Status of the client route enforcement feature, indicating whether Client Route Enforcement is <code>true</code> (enabled) or <code>false</code> (disabled).</p> <p>Valid values: <code>true | false</code> </p> <p>Default value: <code>false</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientRouteEnforcementResponseOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "enforced" in value:
        pairs.append(
            (f"{key_prefix}Enforced", "true" if value["enforced"] else "false")
        )


def deserialize_ec2_query(el: Element) -> ClientRouteEnforcementResponseOptions:
    out: ClientRouteEnforcementResponseOptions = {}  # type: ignore[typeddict-item]
    child_enforced = el.find("enforced")
    if child_enforced is not None:
        out["enforced"] = (child_enforced.text or "").lower() == "true"
    return out
