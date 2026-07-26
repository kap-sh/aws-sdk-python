"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpointConnectionNotificationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class ModifyVpcEndpointConnectionNotificationResult(TypedDict, closed=True):
    return_value: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Returns <code>true</code> if the request succeeds; otherwise, it returns an error.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpcEndpointConnectionNotificationResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "return_value" in value:
        pairs.append((f"{prefix}.Return", "true" if value["return_value"] else "false"))


def deserialize_ec2_query(el: Element) -> ModifyVpcEndpointConnectionNotificationResult:
    out: ModifyVpcEndpointConnectionNotificationResult = {}  # type: ignore[typeddict-item]
    child_return_value = el.find("Return")
    if child_return_value is not None:
        out["return_value"] = (child_return_value.text or "").lower() == "true"
    return out
