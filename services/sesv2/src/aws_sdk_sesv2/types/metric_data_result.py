"""Generated from Smithy shape ``com.amazonaws.sesv2#MetricDataResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.metric_value_list
    import aws_sdk_sesv2.types.query_identifier
    import aws_sdk_sesv2.types.timestamp_list


class MetricDataResult(TypedDict, closed=True):
    id: NotRequired["aws_sdk_sesv2.types.query_identifier.QueryIdentifier"]
    """<p>The query identifier.</p>"""
    timestamps: NotRequired["aws_sdk_sesv2.types.timestamp_list.TimestampList"]
    """<p>A list of timestamps for the metric data results.</p>"""
    values: NotRequired["aws_sdk_sesv2.types.metric_value_list.MetricValueList"]
    """<p>A list of values (cumulative / sum) for the metric data results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricDataResult) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "timestamps" in value:
        import aws_sdk_sesv2.types.timestamp_list

        out["Timestamps"] = aws_sdk_sesv2.types.timestamp_list.serialize_json(
            value["timestamps"]
        )
    if "values" in value:
        import aws_sdk_sesv2.types.metric_value_list

        out["Values"] = aws_sdk_sesv2.types.metric_value_list.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> MetricDataResult:
    out: MetricDataResult = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Timestamps" in data:
        import aws_sdk_sesv2.types.timestamp_list

        out["timestamps"] = aws_sdk_sesv2.types.timestamp_list.deserialize_json(
            data["Timestamps"]
        )
    if "Values" in data:
        import aws_sdk_sesv2.types.metric_value_list

        out["values"] = aws_sdk_sesv2.types.metric_value_list.deserialize_json(
            data["Values"]
        )
    return out
