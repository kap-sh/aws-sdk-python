"""Generated from Smithy shape ``com.amazonaws.sesv2#BatchGetMetricDataQuery``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.dimensions
    import aws_sdk_sesv2.types.metric
    import aws_sdk_sesv2.types.metric_namespace
    import aws_sdk_sesv2.types.query_identifier
    import aws_sdk_sesv2.types.timestamp


class BatchGetMetricDataQuery(TypedDict):
    id: "aws_sdk_sesv2.types.query_identifier.QueryIdentifier"
    """<p>The query identifier.</p>"""
    namespace: "aws_sdk_sesv2.types.metric_namespace.MetricNamespace"
    """<p>The query namespace - e.g. <code>VDM</code> </p>"""
    metric: "aws_sdk_sesv2.types.metric.Metric"
    """<p>The queried metric. This can be one of the following:</p> <ul> <li> <p> <code>SEND</code> – Emails sent eligible for tracking in the VDM dashboard. This excludes emails sent to the mailbox simulator and emails addressed to more than one recipient.</p> </li> <li> <p> <code>COMPLAINT</code> – Complaints received for your account. This excludes complaints from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those for emails addressed to more than one recipient</p> </li> <li> <p> <code>PERMANENT_BOUNCE</code> – Permanent bounces - i.e. feedback received for emails sent to non-existent mailboxes. Excludes bounces from the mailbox simulator, those originating from your account-level suppression list (if enabled), and those for emails addressed to more than one recipient.</p> </li> <li> <p> <code>TRANSIENT_BOUNCE</code> – Transient bounces - i.e. feedback received for delivery failures excluding issues with non-existent mailboxes. Excludes bounces from the mailbox simulator, and those for emails addressed to more than one recipient.</p> </li> <li> <p> <code>OPEN</code> – Unique open events for emails including open trackers. Excludes opens for emails addressed to more than one recipient.</p> </li> <li> <p> <code>CLICK</code> – Unique click events for emails including wrapped links. Excludes clicks for emails addressed to more than one recipient.</p> </li> <li> <p> <code>DELIVERY</code> – Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator and for emails addressed to more than one recipient.</p> </li> <li> <p> <code>DELIVERY_OPEN</code> – Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails without open trackers.</p> </li> <li> <p> <code>DELIVERY_CLICK</code> – Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails without click trackers.</p> </li> <li> <p> <code>DELIVERY_COMPLAINT</code> – Successful deliveries for email sending attempts. Excludes deliveries to the mailbox simulator, for emails addressed to more than one recipient, and emails addressed to recipients hosted by ISPs with which Amazon SES does not have a feedback loop agreement.</p> </li> </ul>"""
    dimensions: NotRequired["aws_sdk_sesv2.types.dimensions.Dimensions"]
    """<p>An object that contains mapping between <code>MetricDimensionName</code> and <code>MetricDimensionValue</code> to filter metrics by.</p>"""
    start_date: "aws_sdk_sesv2.types.timestamp.Timestamp"
    """<p>Represents the start date for the query interval.</p>"""
    end_date: "aws_sdk_sesv2.types.timestamp.Timestamp"
    """<p>Represents the end date for the query interval.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetMetricDataQuery) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import aws_sdk_sesv2.types.metric_namespace

    out["Namespace"] = aws_sdk_sesv2.types.metric_namespace.serialize_json(
        value["namespace"]
    )
    import aws_sdk_sesv2.types.metric

    out["Metric"] = aws_sdk_sesv2.types.metric.serialize_json(value["metric"])
    if "dimensions" in value:
        import aws_sdk_sesv2.types.dimensions

        out["Dimensions"] = aws_sdk_sesv2.types.dimensions.serialize_json(
            value["dimensions"]
        )
    import aws_sdk_sesv2.types.timestamp

    out["StartDate"] = aws_sdk_sesv2.types.timestamp.serialize_json(value["start_date"])
    import aws_sdk_sesv2.types.timestamp

    out["EndDate"] = aws_sdk_sesv2.types.timestamp.serialize_json(value["end_date"])
    return out


def deserialize_json(data: dict) -> BatchGetMetricDataQuery:
    out: BatchGetMetricDataQuery = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("BatchGetMetricDataQuery.id required")
    if "Namespace" in data:
        import aws_sdk_sesv2.types.metric_namespace

        out["namespace"] = aws_sdk_sesv2.types.metric_namespace.deserialize_json(
            data["Namespace"]
        )
    else:
        raise DeserializationError("BatchGetMetricDataQuery.namespace required")
    if "Metric" in data:
        import aws_sdk_sesv2.types.metric

        out["metric"] = aws_sdk_sesv2.types.metric.deserialize_json(data["Metric"])
    else:
        raise DeserializationError("BatchGetMetricDataQuery.metric required")
    if "Dimensions" in data:
        import aws_sdk_sesv2.types.dimensions

        out["dimensions"] = aws_sdk_sesv2.types.dimensions.deserialize_json(
            data["Dimensions"]
        )
    if "StartDate" in data:
        import aws_sdk_sesv2.types.timestamp

        out["start_date"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["StartDate"]
        )
    else:
        raise DeserializationError("BatchGetMetricDataQuery.start_date required")
    if "EndDate" in data:
        import aws_sdk_sesv2.types.timestamp

        out["end_date"] = aws_sdk_sesv2.types.timestamp.deserialize_json(
            data["EndDate"]
        )
    else:
        raise DeserializationError("BatchGetMetricDataQuery.end_date required")
    return out
