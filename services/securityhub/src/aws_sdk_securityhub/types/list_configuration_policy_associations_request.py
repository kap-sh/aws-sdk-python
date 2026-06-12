"""Generated from Smithy shape ``com.amazonaws.securityhub#ListConfigurationPolicyAssociationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.association_filters
    import aws_sdk_securityhub.types.max_results
    import aws_sdk_securityhub.types.next_token


class ListConfigurationPolicyAssociationsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p> The <code>NextToken</code> value that's returned from a previous paginated <code>ListConfigurationPolicyAssociations</code> request where <code>MaxResults</code> was used but the results exceeded the value of that parameter. Pagination continues from the end of the previous response that returned the <code>NextToken</code> value. This value is <code>null</code> when there are no more results to return. </p>"""
    max_results: NotRequired["aws_sdk_securityhub.types.max_results.MaxResults"]
    """<p> The maximum number of results that's returned by <code>ListConfigurationPolicies</code> in each page of the response. When this parameter is used, <code>ListConfigurationPolicyAssociations</code> returns the specified number of results in a single page and a <code>NextToken</code> response element. You can see the remaining results of the initial request by sending another <code>ListConfigurationPolicyAssociations</code> request with the returned <code>NextToken</code> value. A valid range for <code>MaxResults</code> is between 1 and 100. </p>"""
    filters: NotRequired[
        "aws_sdk_securityhub.types.association_filters.AssociationFilters"
    ]
    """<p> Options for filtering the <code>ListConfigurationPolicyAssociations</code> response. You can filter by the Amazon Resource Name (ARN) or universally unique identifier (UUID) of a configuration, <code>AssociationType</code>, or <code>AssociationStatus</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfigurationPolicyAssociationsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import aws_sdk_securityhub.types.association_filters

        out["Filters"] = aws_sdk_securityhub.types.association_filters.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> ListConfigurationPolicyAssociationsRequest:
    out: ListConfigurationPolicyAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Filters" in data:
        import aws_sdk_securityhub.types.association_filters

        out["filters"] = aws_sdk_securityhub.types.association_filters.deserialize_json(
            data["Filters"]
        )
    return out
