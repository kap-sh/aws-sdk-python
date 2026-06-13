"""Generated from Smithy shape ``com.amazonaws.ssmincidents#IncidentRecordSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.incident_record_summary

IncidentRecordSummaryList: TypeAlias = list[
    "aws_sdk_ssm_incidents.types.incident_record_summary.IncidentRecordSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: IncidentRecordSummaryList) -> list:
    import aws_sdk_ssm_incidents.types.incident_record_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ssm_incidents.types.incident_record_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> IncidentRecordSummaryList:
    import aws_sdk_ssm_incidents.types.incident_record_summary

    out: IncidentRecordSummaryList = []
    for item in data:
        out.append(
            aws_sdk_ssm_incidents.types.incident_record_summary.deserialize_json(item)
        )
    return out
