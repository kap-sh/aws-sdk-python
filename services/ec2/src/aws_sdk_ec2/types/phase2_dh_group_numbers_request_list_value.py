"""Generated from Smithy shape ``com.amazonaws.ec2#Phase2DHGroupNumbersRequestListValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.integer


class Phase2DHGroupNumbersRequestListValue(TypedDict):
    value: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The Diffie-Hellmann group number.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Phase2DHGroupNumbersRequestListValue,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))


def deserialize_ec2_query(el: Element) -> Phase2DHGroupNumbersRequestListValue:
    out: Phase2DHGroupNumbersRequestListValue = {}  # type: ignore[typeddict-item]
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = int(child_value.text or "")
    return out
