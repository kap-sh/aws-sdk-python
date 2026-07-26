"""Generated from Smithy shape ``com.amazonaws.securityhub#GetFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_security_finding_filters
    import capo_securityhub.types.max_results
    import capo_securityhub.types.next_token
    import capo_securityhub.types.sort_criteria


class GetFindingsRequest(TypedDict, closed=True):
    filters: NotRequired[
        "capo_securityhub.types.aws_security_finding_filters.AwsSecurityFindingFilters"
    ]
    """<p>The finding attributes used to define a condition to filter the returned findings.</p> <p>You can filter by up to 10 finding attributes. For each attribute, you can provide up to 20 filter values.</p> <p>Note that in the available filter fields, <code>WorkflowState</code> is deprecated. To search for a finding based on its workflow status, use <code>WorkflowStatus</code>.</p>"""
    sort_criteria: NotRequired["capo_securityhub.types.sort_criteria.SortCriteria"]
    """<p>The finding attributes used to sort the list of returned findings.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The token that is required for pagination. On your first call to the <code>GetFindings</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>"""
    max_results: NotRequired["capo_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of findings to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_securityhub.types.aws_security_finding_filters

        out["Filters"] = (
            capo_securityhub.types.aws_security_finding_filters.serialize_json(
                value["filters"]
            )
        )
    if "sort_criteria" in value:
        import capo_securityhub.types.sort_criteria

        out["SortCriteria"] = capo_securityhub.types.sort_criteria.serialize_json(
            value["sort_criteria"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> GetFindingsRequest:
    out: GetFindingsRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import capo_securityhub.types.aws_security_finding_filters

        out["filters"] = (
            capo_securityhub.types.aws_security_finding_filters.deserialize_json(
                data["Filters"]
            )
        )
    if "SortCriteria" in data:
        import capo_securityhub.types.sort_criteria

        out["sort_criteria"] = capo_securityhub.types.sort_criteria.deserialize_json(
            data["SortCriteria"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
