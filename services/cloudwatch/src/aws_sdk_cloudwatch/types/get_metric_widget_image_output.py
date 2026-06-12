"""Generated from Smithy shape ``com.amazonaws.cloudwatch#GetMetricWidgetImageOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.metric_widget_image


class GetMetricWidgetImageOutput(TypedDict):
    metric_widget_image: NotRequired[
        "aws_sdk_cloudwatch.types.metric_widget_image.MetricWidgetImage"
    ]
    """<p>The image of the graph, in the output format specified. The output is base64-encoded.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetMetricWidgetImageOutput) -> dict:
    out: dict = {}
    if "metric_widget_image" in value:
        import aws_sdk_cloudwatch.types.metric_widget_image

        out["MetricWidgetImage"] = (
            aws_sdk_cloudwatch.types.metric_widget_image.serialize_aws_json_1_0(
                value["metric_widget_image"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetMetricWidgetImageOutput:
    out: GetMetricWidgetImageOutput = {}  # type: ignore[typeddict-item]
    if "MetricWidgetImage" in data:
        import aws_sdk_cloudwatch.types.metric_widget_image

        out["metric_widget_image"] = (
            aws_sdk_cloudwatch.types.metric_widget_image.deserialize_aws_json_1_0(
                data["MetricWidgetImage"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: GetMetricWidgetImageOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "metric_widget_image" in value:
        import aws_sdk_cloudwatch.types.metric_widget_image

        aws_sdk_cloudwatch.types.metric_widget_image.serialize_query(
            value["metric_widget_image"], pairs, f"{prefix}.MetricWidgetImage"
        )


def deserialize_query(el: Element) -> GetMetricWidgetImageOutput:
    out: GetMetricWidgetImageOutput = {}  # type: ignore[typeddict-item]
    child_metric_widget_image = el.find("MetricWidgetImage")
    if child_metric_widget_image is not None:
        import aws_sdk_cloudwatch.types.metric_widget_image

        out["metric_widget_image"] = (
            aws_sdk_cloudwatch.types.metric_widget_image.deserialize_query(
                child_metric_widget_image
            )
        )
    return out
