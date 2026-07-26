"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ListEngagementsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_contacts.types.incident_id
    import capo_ssm_contacts.types.max_results
    import capo_ssm_contacts.types.pagination_token
    import capo_ssm_contacts.types.time_range


class ListEngagementsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_ssm_contacts.types.pagination_token.PaginationToken"]
    """<p>The pagination token to continue to the next page of results.</p>"""
    max_results: NotRequired["capo_ssm_contacts.types.max_results.MaxResults"]
    """<p>The maximum number of engagements per page of results.</p>"""
    incident_id: NotRequired["capo_ssm_contacts.types.incident_id.IncidentId"]
    """<p>The Amazon Resource Name (ARN) of the incident you're listing engagements for.</p>"""
    time_range_value: NotRequired["capo_ssm_contacts.types.time_range.TimeRange"]
    """<p>The time range to lists engagements for an incident.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEngagementsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "incident_id" in value:
        out["IncidentId"] = value["incident_id"]
    if "time_range_value" in value:
        import capo_ssm_contacts.types.time_range

        out["TimeRangeValue"] = (
            capo_ssm_contacts.types.time_range.serialize_aws_json_1_1(
                value["time_range_value"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEngagementsRequest:
    out: ListEngagementsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "IncidentId" in data:
        out["incident_id"] = data["IncidentId"]
    if "TimeRangeValue" in data:
        import capo_ssm_contacts.types.time_range

        out["time_range_value"] = (
            capo_ssm_contacts.types.time_range.deserialize_aws_json_1_1(
                data["TimeRangeValue"]
            )
        )
    return out
