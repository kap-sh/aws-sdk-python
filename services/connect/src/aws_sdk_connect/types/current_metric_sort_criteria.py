"""Generated from Smithy shape ``com.amazonaws.connect#CurrentMetricSortCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.current_metric_name
    import aws_sdk_connect.types.sort_order


class CurrentMetricSortCriteria(TypedDict):
    sort_by_metric: NotRequired[
        "aws_sdk_connect.types.current_metric_name.CurrentMetricName"
    ]
    sort_order: NotRequired["aws_sdk_connect.types.sort_order.SortOrder"]
    """<p>The way to sort.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CurrentMetricSortCriteria) -> dict:
    out: dict = {}
    if "sort_by_metric" in value:
        import aws_sdk_connect.types.current_metric_name

        out["SortByMetric"] = aws_sdk_connect.types.current_metric_name.serialize_json(
            value["sort_by_metric"]
        )
    if "sort_order" in value:
        import aws_sdk_connect.types.sort_order

        out["SortOrder"] = aws_sdk_connect.types.sort_order.serialize_json(
            value["sort_order"]
        )
    return out


def deserialize_json(data: dict) -> CurrentMetricSortCriteria:
    out: CurrentMetricSortCriteria = {}  # type: ignore[typeddict-item]
    if "SortByMetric" in data:
        import aws_sdk_connect.types.current_metric_name

        out["sort_by_metric"] = (
            aws_sdk_connect.types.current_metric_name.deserialize_json(
                data["SortByMetric"]
            )
        )
    if "SortOrder" in data:
        import aws_sdk_connect.types.sort_order

        out["sort_order"] = aws_sdk_connect.types.sort_order.deserialize_json(
            data["SortOrder"]
        )
    return out
