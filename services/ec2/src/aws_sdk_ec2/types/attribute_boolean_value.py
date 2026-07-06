"""Generated from Smithy shape ``com.amazonaws.ec2#AttributeBooleanValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean


class AttributeBooleanValue(TypedDict, closed=True):
    value: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The attribute value. The valid values are <code>true</code> or <code>false</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AttributeBooleanValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "value" in value:
        pairs.append((f"{prefix}.Value", "true" if value["value"] else "false"))


def deserialize_ec2_query(el: Element) -> AttributeBooleanValue:
    out: AttributeBooleanValue = {}  # type: ignore[typeddict-item]
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = (child_value.text or "").lower() == "true"
    return out
