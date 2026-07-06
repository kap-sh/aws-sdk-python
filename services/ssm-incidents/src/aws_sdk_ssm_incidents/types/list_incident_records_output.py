"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ListIncidentRecordsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.incident_record_summary_list
    import aws_sdk_ssm_incidents.types.next_token


class ListIncidentRecordsOutput(TypedDict, closed=True):
    incident_record_summaries: "aws_sdk_ssm_incidents.types.incident_record_summary_list.IncidentRecordSummaryList"
    """<p>The details of each listed incident record.</p>"""
    next_token: NotRequired["aws_sdk_ssm_incidents.types.next_token.NextToken"]
    """<p>The pagination token to use when requesting the next set of items. If there are no additional items to return, the string is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIncidentRecordsOutput) -> dict:
    out: dict = {}
    import aws_sdk_ssm_incidents.types.incident_record_summary_list

    out["incidentRecordSummaries"] = (
        aws_sdk_ssm_incidents.types.incident_record_summary_list.serialize_json(
            value["incident_record_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIncidentRecordsOutput:
    out: ListIncidentRecordsOutput = {}  # type: ignore[typeddict-item]
    if "incidentRecordSummaries" in data:
        import aws_sdk_ssm_incidents.types.incident_record_summary_list

        out["incident_record_summaries"] = (
            aws_sdk_ssm_incidents.types.incident_record_summary_list.deserialize_json(
                data["incidentRecordSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListIncidentRecordsOutput.incident_record_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
