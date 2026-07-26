"""Generated from Smithy shape ``com.amazonaws.autoscaling#AdjustmentType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.xml_string_max_len255


class AdjustmentType(TypedDict, closed=True):
    adjustment_type: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The policy adjustment type. The valid values are <code>ChangeInCapacity</code>, <code>ExactCapacity</code>, and <code>PercentChangeInCapacity</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: AdjustmentType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "adjustment_type" in value:
        pairs.append((f"{prefix}.AdjustmentType", str(value["adjustment_type"])))


def deserialize_query(el: Element) -> AdjustmentType:
    out: AdjustmentType = {}  # type: ignore[typeddict-item]
    child_adjustment_type = el.find("AdjustmentType")
    if child_adjustment_type is not None:
        out["adjustment_type"] = str(child_adjustment_type.text or "")
    return out
