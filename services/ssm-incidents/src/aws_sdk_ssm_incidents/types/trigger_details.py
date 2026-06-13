"""Generated from Smithy shape ``com.amazonaws.ssmincidents#TriggerDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.incident_source
    import aws_sdk_ssm_incidents.types.raw_data


class TriggerDetails(TypedDict):
    source: "aws_sdk_ssm_incidents.types.incident_source.IncidentSource"
    """<p>Identifies the service that sourced the event. All events sourced from within Amazon Web Services begin with \"<code>aws.</code>\" Customer-generated events can have any value here, as long as it doesn't begin with \"<code>aws.</code>\" We recommend the use of Java package-name style reverse domain-name strings. </p>"""
    trigger_arn: NotRequired["aws_sdk_ssm_incidents.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the source that detected the incident.</p>"""
    timestamp: "datetime.datetime"
    """<p>The timestamp for when the incident was detected.</p>"""
    raw_data: NotRequired["aws_sdk_ssm_incidents.types.raw_data.RawData"]
    """<p>Raw data passed from either Amazon EventBridge, Amazon CloudWatch, or Incident Manager when an incident is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TriggerDetails) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    if "trigger_arn" in value:
        out["triggerArn"] = value["trigger_arn"]
    import aws_sdk_ssm_incidents.types._prelude.timestamp

    out["timestamp"] = aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    if "raw_data" in value:
        out["rawData"] = value["raw_data"]
    return out


def deserialize_json(data: dict) -> TriggerDetails:
    out: TriggerDetails = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("TriggerDetails.source required")
    if "triggerArn" in data:
        out["trigger_arn"] = data["triggerArn"]
    if "timestamp" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["timestamp"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["timestamp"]
            )
        )
    else:
        raise DeserializationError("TriggerDetails.timestamp required")
    if "rawData" in data:
        out["raw_data"] = data["rawData"]
    return out
