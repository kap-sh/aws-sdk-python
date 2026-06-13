"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ListIncidentFindingsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.next_token


class ListIncidentFindingsInput(TypedDict):
    incident_record_arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident for which you want to view associated findings.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of findings to retrieve per call.</p>"""
    next_token: NotRequired["aws_sdk_ssm_incidents.types.next_token.NextToken"]
    """<p>The pagination token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIncidentFindingsInput) -> dict:
    out: dict = {}
    out["incidentRecordArn"] = value["incident_record_arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIncidentFindingsInput:
    out: ListIncidentFindingsInput = {}  # type: ignore[typeddict-item]
    if "incidentRecordArn" in data:
        out["incident_record_arn"] = data["incidentRecordArn"]
    else:
        raise DeserializationError(
            "ListIncidentFindingsInput.incident_record_arn required"
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
