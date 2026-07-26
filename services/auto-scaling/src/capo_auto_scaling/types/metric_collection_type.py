"""Generated from Smithy shape ``com.amazonaws.autoscaling#MetricCollectionType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.xml_string_max_len255


class MetricCollectionType(TypedDict, closed=True):
    metric: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>One of the following metrics:</p> <ul> <li> <p> <code>GroupMinSize</code> </p> </li> <li> <p> <code>GroupMaxSize</code> </p> </li> <li> <p> <code>GroupDesiredCapacity</code> </p> </li> <li> <p> <code>GroupInServiceInstances</code> </p> </li> <li> <p> <code>GroupPendingInstances</code> </p> </li> <li> <p> <code>GroupStandbyInstances</code> </p> </li> <li> <p> <code>GroupTerminatingInstances</code> </p> </li> <li> <p> <code>GroupTotalInstances</code> </p> </li> <li> <p> <code>GroupInServiceCapacity</code> </p> </li> <li> <p> <code>GroupPendingCapacity</code> </p> </li> <li> <p> <code>GroupStandbyCapacity</code> </p> </li> <li> <p> <code>GroupTerminatingCapacity</code> </p> </li> <li> <p> <code>GroupTotalCapacity</code> </p> </li> <li> <p> <code>WarmPoolDesiredCapacity</code> </p> </li> <li> <p> <code>WarmPoolWarmedCapacity</code> </p> </li> <li> <p> <code>WarmPoolPendingCapacity</code> </p> </li> <li> <p> <code>WarmPoolTerminatingCapacity</code> </p> </li> <li> <p> <code>WarmPoolTotalCapacity</code> </p> </li> <li> <p> <code>GroupAndWarmPoolDesiredCapacity</code> </p> </li> <li> <p> <code>GroupAndWarmPoolTotalCapacity</code> </p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricCollectionType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "metric" in value:
        pairs.append((f"{prefix}.Metric", str(value["metric"])))


def deserialize_query(el: Element) -> MetricCollectionType:
    out: MetricCollectionType = {}  # type: ignore[typeddict-item]
    child_metric = el.find("Metric")
    if child_metric is not None:
        out["metric"] = str(child_metric.text or "")
    return out
