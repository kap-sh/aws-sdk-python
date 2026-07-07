"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ListIncidentFindingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.finding_summary_list
    import aws_sdk_ssm_incidents.types.next_token


class ListIncidentFindingsOutput(TypedDict, closed=True):
    findings: "aws_sdk_ssm_incidents.types.finding_summary_list.FindingSummaryList"
    """<p>A list of findings that represent deployments that might be the potential cause of the incident.</p>"""
    next_token: NotRequired["aws_sdk_ssm_incidents.types.next_token.NextToken"]
    """<p>The pagination token to use when requesting the next set of items. If there are no additional items to return, the string is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIncidentFindingsOutput) -> dict:
    out: dict = {}
    import aws_sdk_ssm_incidents.types.finding_summary_list

    out["findings"] = aws_sdk_ssm_incidents.types.finding_summary_list.serialize_json(
        value["findings"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIncidentFindingsOutput:
    out: ListIncidentFindingsOutput = {}  # type: ignore[typeddict-item]
    if "findings" in data:
        import aws_sdk_ssm_incidents.types.finding_summary_list

        out["findings"] = (
            aws_sdk_ssm_incidents.types.finding_summary_list.deserialize_json(
                data["findings"]
            )
        )
    else:
        raise DeserializationError("ListIncidentFindingsOutput.findings required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
