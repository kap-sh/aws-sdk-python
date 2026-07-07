"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ListRelatedItemsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.max_results
    import aws_sdk_ssm_incidents.types.next_token


class ListRelatedItemsInput(TypedDict, closed=True):
    incident_record_arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident record containing the listed related items.</p>"""
    max_results: NotRequired["aws_sdk_ssm_incidents.types.max_results.MaxResults"]
    """<p>The maximum number of related items per page.</p>"""
    next_token: NotRequired["aws_sdk_ssm_incidents.types.next_token.NextToken"]
    """<p>The pagination token for the next set of items to return. (You received this token from a previous call.)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRelatedItemsInput) -> dict:
    out: dict = {}
    out["incidentRecordArn"] = value["incident_record_arn"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRelatedItemsInput:
    out: ListRelatedItemsInput = {}  # type: ignore[typeddict-item]
    if "incidentRecordArn" in data:
        out["incident_record_arn"] = data["incidentRecordArn"]
    else:
        raise DeserializationError("ListRelatedItemsInput.incident_record_arn required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
