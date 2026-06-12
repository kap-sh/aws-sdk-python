"""Generated from Smithy shape ``com.amazonaws.securityhub#GetResourcesV2Request``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.max_results
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.resource_scopes
    import aws_sdk_securityhub.types.resources_filters
    import aws_sdk_securityhub.types.sort_criteria


class GetResourcesV2Request(TypedDict):
    filters: NotRequired["aws_sdk_securityhub.types.resources_filters.ResourcesFilters"]
    """<p>Filters resources based on a set of criteria.</p>"""
    scopes: NotRequired["aws_sdk_securityhub.types.resource_scopes.ResourceScopes"]
    """<p>Limits the results to resources from specific organizational units or from the delegated administrator's organization. Only the delegated administrator account can use this parameter. Other accounts receive an <code>AccessDeniedException</code>.</p> <p>This parameter is optional. If you omit it, the delegated administrator sees resources from all accounts across the entire organization. Other accounts see only their own resources.</p> <p>You can specify up to 10 entries in <code>Scopes.AwsOrganizations</code>. If multiple entries are specified, the entries are combined using OR logic.</p>"""
    sort_criteria: NotRequired["aws_sdk_securityhub.types.sort_criteria.SortCriteria"]
    """<p>The resource attributes used to sort the list of returned resources.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The token required for pagination. On your first call, set the value of this parameter to <code>NULL</code>. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.</p>"""
    max_results: NotRequired["aws_sdk_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResourcesV2Request) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_securityhub.types.resources_filters

        out["Filters"] = aws_sdk_securityhub.types.resources_filters.serialize_json(
            value["filters"]
        )
    if "scopes" in value:
        import aws_sdk_securityhub.types.resource_scopes

        out["Scopes"] = aws_sdk_securityhub.types.resource_scopes.serialize_json(
            value["scopes"]
        )
    if "sort_criteria" in value:
        import aws_sdk_securityhub.types.sort_criteria

        out["SortCriteria"] = aws_sdk_securityhub.types.sort_criteria.serialize_json(
            value["sort_criteria"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> GetResourcesV2Request:
    out: GetResourcesV2Request = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_securityhub.types.resources_filters

        out["filters"] = aws_sdk_securityhub.types.resources_filters.deserialize_json(
            data["Filters"]
        )
    if "Scopes" in data:
        import aws_sdk_securityhub.types.resource_scopes

        out["scopes"] = aws_sdk_securityhub.types.resource_scopes.deserialize_json(
            data["Scopes"]
        )
    if "SortCriteria" in data:
        import aws_sdk_securityhub.types.sort_criteria

        out["sort_criteria"] = aws_sdk_securityhub.types.sort_criteria.deserialize_json(
            data["SortCriteria"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
