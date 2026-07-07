"""Generated from Smithy shape ``com.amazonaws.autoscaling#MetricDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.metric_dimension_name
    import aws_sdk_auto_scaling.types.metric_dimension_value


class MetricDimension(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_auto_scaling.types.metric_dimension_name.MetricDimensionName"
    ]
    """<p>The name of the dimension.</p>"""
    value: NotRequired[
        "aws_sdk_auto_scaling.types.metric_dimension_value.MetricDimensionValue"
    ]
    """<p>The value of the dimension.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricDimension, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "value" in value:
        pairs.append((f"{prefix}.Value", str(value["value"])))


def deserialize_query(el: Element) -> MetricDimension:
    out: MetricDimension = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
