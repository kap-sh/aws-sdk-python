"""Generated from Smithy shape ``com.amazonaws.xray#SamplingBoostStatisticsDocument``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.anomaly_count
    import aws_sdk_xray.types.rule_name
    import aws_sdk_xray.types.sampled_anomaly_count
    import aws_sdk_xray.types.service_name
    import aws_sdk_xray.types.timestamp
    import aws_sdk_xray.types.total_count


class SamplingBoostStatisticsDocument(TypedDict):
    rule_name: "aws_sdk_xray.types.rule_name.RuleName"
    """<p>The name of the sampling rule.</p>"""
    service_name: "aws_sdk_xray.types.service_name.ServiceName"
    """<p>Matches the <code>name</code> that the service uses to identify itself in segments.</p>"""
    timestamp: "aws_sdk_xray.types.timestamp.Timestamp"
    """<p>The current time.</p>"""
    anomaly_count: "aws_sdk_xray.types.anomaly_count.AnomalyCount"
    """<p>The number of requests with anomaly.</p>"""
    total_count: "aws_sdk_xray.types.total_count.TotalCount"
    """<p>The number of requests that associated to the rule.</p>"""
    sampled_anomaly_count: (
        "aws_sdk_xray.types.sampled_anomaly_count.SampledAnomalyCount"
    )
    """<p>The number of requests with anomaly recorded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamplingBoostStatisticsDocument) -> dict:
    out: dict = {}
    out["RuleName"] = value["rule_name"]
    out["ServiceName"] = value["service_name"]
    import aws_sdk_xray.types.timestamp

    out["Timestamp"] = aws_sdk_xray.types.timestamp.serialize_json(value["timestamp"])
    out["AnomalyCount"] = value.get("anomaly_count", 0)
    out["TotalCount"] = value.get("total_count", 0)
    out["SampledAnomalyCount"] = value.get("sampled_anomaly_count", 0)
    return out


def deserialize_json(data: dict) -> SamplingBoostStatisticsDocument:
    out: SamplingBoostStatisticsDocument = {}  # type: ignore[typeddict-item]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    else:
        raise DeserializationError("SamplingBoostStatisticsDocument.rule_name required")
    if "ServiceName" in data:
        out["service_name"] = data["ServiceName"]
    else:
        raise DeserializationError(
            "SamplingBoostStatisticsDocument.service_name required"
        )
    if "Timestamp" in data:
        import aws_sdk_xray.types.timestamp

        out["timestamp"] = aws_sdk_xray.types.timestamp.deserialize_json(
            data["Timestamp"]
        )
    else:
        raise DeserializationError("SamplingBoostStatisticsDocument.timestamp required")
    if "AnomalyCount" in data:
        out["anomaly_count"] = data["AnomalyCount"]
    else:
        out["anomaly_count"] = 0
    if "TotalCount" in data:
        out["total_count"] = data["TotalCount"]
    else:
        out["total_count"] = 0
    if "SampledAnomalyCount" in data:
        out["sampled_anomaly_count"] = data["SampledAnomalyCount"]
    else:
        out["sampled_anomaly_count"] = 0
    return out
