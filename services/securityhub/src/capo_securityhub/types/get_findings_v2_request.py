"""Generated from Smithy shape ``com.amazonaws.securityhub#GetFindingsV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.finding_scopes
    import capo_securityhub.types.max_results
    import capo_securityhub.types.next_token
    import capo_securityhub.types.ocsf_finding_filters
    import capo_securityhub.types.sort_criteria


class GetFindingsV2Request(TypedDict, closed=True):
    filters: NotRequired[
        "capo_securityhub.types.ocsf_finding_filters.OcsfFindingFilters"
    ]
    """<p>The finding attributes used to define a condition to filter the returned OCSF findings. You can filter up to 10 composite filters. For each filter type inside of a composite filter, you can provide up to 20 filters.</p>"""
    scopes: NotRequired["capo_securityhub.types.finding_scopes.FindingScopes"]
    """<p>Limits the results to findings from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an <code>AccessDeniedException</code>.</p> <p>This parameter is optional. If you omit it, the delegated administrator sees findings from all accounts across the entire organization. Other accounts see only their own findings.</p> <p>You can specify up to 10 entries in <code>Scopes.AwsOrganizations</code>. If multiple entries are specified, the entries are combined using OR logic.</p>"""
    sort_criteria: NotRequired["capo_securityhub.types.sort_criteria.SortCriteria"]
    """<p>The finding attributes used to sort the list of returned findings.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p> The token required for pagination. On your first call, set the value of this parameter to <code>NULL</code>. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.</p>"""
    max_results: NotRequired["capo_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsV2Request) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_securityhub.types.ocsf_finding_filters

        out["Filters"] = capo_securityhub.types.ocsf_finding_filters.serialize_json(
            value["filters"]
        )
    if "scopes" in value:
        import capo_securityhub.types.finding_scopes

        out["Scopes"] = capo_securityhub.types.finding_scopes.serialize_json(
            value["scopes"]
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


def deserialize_json(data: dict) -> GetFindingsV2Request:
    out: GetFindingsV2Request = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import capo_securityhub.types.ocsf_finding_filters

        out["filters"] = capo_securityhub.types.ocsf_finding_filters.deserialize_json(
            data["Filters"]
        )
    if "Scopes" in data:
        import capo_securityhub.types.finding_scopes

        out["scopes"] = capo_securityhub.types.finding_scopes.deserialize_json(
            data["Scopes"]
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
