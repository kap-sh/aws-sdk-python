"""Generated from Smithy shape ``com.amazonaws.ec2#Phase2IntegrityAlgorithmsRequestListValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class Phase2IntegrityAlgorithmsRequestListValue(TypedDict, closed=True):
    value: NotRequired["capo_ec2.types.string.String"]
    """<p>The integrity algorithm.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Phase2IntegrityAlgorithmsRequestListValue,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))


def deserialize_ec2_query(el: Element) -> Phase2IntegrityAlgorithmsRequestListValue:
    out: Phase2IntegrityAlgorithmsRequestListValue = {}  # type: ignore[typeddict-item]
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
