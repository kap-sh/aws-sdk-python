"""Generated from Smithy shape ``com.amazonaws.ec2#AlternatePathHint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class AlternatePathHint(TypedDict, closed=True):
    component_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the component.</p>"""
    component_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the component.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AlternatePathHint, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "component_id" in value:
        pairs.append((f"{prefix}.ComponentId", str(value["component_id"])))
    if "component_arn" in value:
        pairs.append((f"{prefix}.ComponentArn", str(value["component_arn"])))


def deserialize_ec2_query(el: Element) -> AlternatePathHint:
    out: AlternatePathHint = {}  # type: ignore[typeddict-item]
    child_component_id = el.find("ComponentId")
    if child_component_id is not None:
        out["component_id"] = str(child_component_id.text or "")
    child_component_arn = el.find("ComponentArn")
    if child_component_arn is not None:
        out["component_arn"] = str(child_component_arn.text or "")
    return out
