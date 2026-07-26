"""Generated from Smithy shape ``com.amazonaws.autoscaling#MetricGranularityType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.xml_string_max_len255


class MetricGranularityType(TypedDict, closed=True):
    granularity: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The granularity. The only valid value is <code>1Minute</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricGranularityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "granularity" in value:
        pairs.append((f"{prefix}.Granularity", str(value["granularity"])))


def deserialize_query(el: Element) -> MetricGranularityType:
    out: MetricGranularityType = {}  # type: ignore[typeddict-item]
    child_granularity = el.find("Granularity")
    if child_granularity is not None:
        out["granularity"] = str(child_granularity.text or "")
    return out
