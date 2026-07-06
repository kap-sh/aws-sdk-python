"""Generated from Smithy shape ``com.amazonaws.ssmincidents#IncidentRecordSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.impact
    import aws_sdk_ssm_incidents.types.incident_record_source
    import aws_sdk_ssm_incidents.types.incident_record_status
    import aws_sdk_ssm_incidents.types.incident_title


class IncidentRecordSummary(TypedDict, closed=True):
    arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident.</p>"""
    title: "aws_sdk_ssm_incidents.types.incident_title.IncidentTitle"
    """<p>The title of the incident. This value is either provided by the response plan or overwritten on creation.</p>"""
    status: "aws_sdk_ssm_incidents.types.incident_record_status.IncidentRecordStatus"
    """<p>The current status of the incident.</p>"""
    impact: "aws_sdk_ssm_incidents.types.impact.Impact"
    """<p>Defines the impact to customers and applications.</p>"""
    creation_time: "datetime.datetime"
    """<p>The timestamp for when the incident was created.</p>"""
    resolved_time: NotRequired["datetime.datetime"]
    """<p>The timestamp for when the incident was resolved.</p>"""
    incident_record_source: (
        "aws_sdk_ssm_incidents.types.incident_record_source.IncidentRecordSource"
    )
    """<p>What caused Incident Manager to create the incident.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncidentRecordSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["title"] = value["title"]
    out["status"] = value["status"]
    out["impact"] = value["impact"]
    import aws_sdk_ssm_incidents.types._prelude.timestamp

    out["creationTime"] = aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "resolved_time" in value:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["resolvedTime"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
                value["resolved_time"]
            )
        )
    import aws_sdk_ssm_incidents.types.incident_record_source

    out["incidentRecordSource"] = (
        aws_sdk_ssm_incidents.types.incident_record_source.serialize_json(
            value["incident_record_source"]
        )
    )
    return out


def deserialize_json(data: dict) -> IncidentRecordSummary:
    out: IncidentRecordSummary = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IncidentRecordSummary.arn required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("IncidentRecordSummary.title required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("IncidentRecordSummary.status required")
    if "impact" in data:
        out["impact"] = data["impact"]
    else:
        raise DeserializationError("IncidentRecordSummary.impact required")
    if "creationTime" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("IncidentRecordSummary.creation_time required")
    if "resolvedTime" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["resolved_time"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["resolvedTime"]
            )
        )
    if "incidentRecordSource" in data:
        import aws_sdk_ssm_incidents.types.incident_record_source

        out["incident_record_source"] = (
            aws_sdk_ssm_incidents.types.incident_record_source.deserialize_json(
                data["incidentRecordSource"]
            )
        )
    else:
        raise DeserializationError(
            "IncidentRecordSummary.incident_record_source required"
        )
    return out
