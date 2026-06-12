"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#Anomaly``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.anomaly_instances
    import aws_sdk_codeguruprofiler.types.metric


class Anomaly(TypedDict):
    metric: "aws_sdk_codeguruprofiler.types.metric.Metric"
    """<p> Details about the metric that the analysis used when it detected the anomaly. The metric includes the name of the frame that was analyzed with the type and thread states used to derive the metric value for that frame. </p>"""
    reason: "str"
    """<p>The reason for which metric was flagged as anomalous.</p>"""
    instances: "aws_sdk_codeguruprofiler.types.anomaly_instances.AnomalyInstances"
    """<p> A list of the instances of the detected anomalies during the requested period. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Anomaly) -> dict:
    out: dict = {}
    import aws_sdk_codeguruprofiler.types.metric

    out["metric"] = aws_sdk_codeguruprofiler.types.metric.serialize_json(
        value["metric"]
    )
    out["reason"] = value["reason"]
    import aws_sdk_codeguruprofiler.types.anomaly_instances

    out["instances"] = aws_sdk_codeguruprofiler.types.anomaly_instances.serialize_json(
        value["instances"]
    )
    return out


def deserialize_json(data: dict) -> Anomaly:
    out: Anomaly = {}  # type: ignore[typeddict-item]
    if "metric" in data:
        import aws_sdk_codeguruprofiler.types.metric

        out["metric"] = aws_sdk_codeguruprofiler.types.metric.deserialize_json(
            data["metric"]
        )
    else:
        raise DeserializationError("Anomaly.metric required")
    if "reason" in data:
        out["reason"] = data["reason"]
    else:
        raise DeserializationError("Anomaly.reason required")
    if "instances" in data:
        import aws_sdk_codeguruprofiler.types.anomaly_instances

        out["instances"] = (
            aws_sdk_codeguruprofiler.types.anomaly_instances.deserialize_json(
                data["instances"]
            )
        )
    else:
        raise DeserializationError("Anomaly.instances required")
    return out
