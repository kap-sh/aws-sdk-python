"""Generated from Smithy shape ``com.amazonaws.pi#MetricDimensionGroups``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pi.types.dimension_group_detail_list
    import aws_sdk_pi.types.string


class MetricDimensionGroups(TypedDict):
    metric: NotRequired["aws_sdk_pi.types.string.String"]
    """<p>The metric type to which the dimension information belongs.</p>"""
    groups: NotRequired[
        "aws_sdk_pi.types.dimension_group_detail_list.DimensionGroupDetailList"
    ]
    """<p>The available dimension groups for a metric type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDimensionGroups) -> dict:
    out: dict = {}
    if "metric" in value:
        out["Metric"] = value["metric"]
    if "groups" in value:
        import aws_sdk_pi.types.dimension_group_detail_list

        out["Groups"] = (
            aws_sdk_pi.types.dimension_group_detail_list.serialize_aws_json_1_1(
                value["groups"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricDimensionGroups:
    out: MetricDimensionGroups = {}  # type: ignore[typeddict-item]
    if "Metric" in data:
        out["metric"] = data["Metric"]
    if "Groups" in data:
        import aws_sdk_pi.types.dimension_group_detail_list

        out["groups"] = (
            aws_sdk_pi.types.dimension_group_detail_list.deserialize_aws_json_1_1(
                data["Groups"]
            )
        )
    return out
