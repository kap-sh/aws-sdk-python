"""Generated from Smithy shape ``com.amazonaws.mwaa#PublishMetricsInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_mwaa.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mwaa.types.environment_name
    import aws_sdk_mwaa.types.metric_data


class PublishMetricsInput(TypedDict):
    environment_name: "aws_sdk_mwaa.types.environment_name.EnvironmentName"
    """<p> <b>Internal only</b>. The name of the environment.</p>"""
    metric_data: "aws_sdk_mwaa.types.metric_data.MetricData"
    r"""<p> <b>Internal only</b>. Publishes metrics to Amazon CloudWatch. To learn more about the metrics published to Amazon CloudWatch, see <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/cw-metrics.html\">Amazon MWAA performance metrics in Amazon CloudWatch</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishMetricsInput) -> dict:
    out: dict = {}
    import aws_sdk_mwaa.types.metric_data

    out["MetricData"] = aws_sdk_mwaa.types.metric_data.serialize_json(
        value["metric_data"]
    )
    return out


def deserialize_json(data: dict) -> PublishMetricsInput:
    out: PublishMetricsInput = {}  # type: ignore[typeddict-item]
    if "MetricData" in data:
        import aws_sdk_mwaa.types.metric_data

        out["metric_data"] = aws_sdk_mwaa.types.metric_data.deserialize_json(
            data["MetricData"]
        )
    else:
        raise DeserializationError("PublishMetricsInput.metric_data required")
    return out
