"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListGroupResourcesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.group_name
    import capo_resource_groups.types.group_string_v2
    import capo_resource_groups.types.max_results
    import capo_resource_groups.types.next_token
    import capo_resource_groups.types.resource_filter_list


class ListGroupResourcesInput(TypedDict, closed=True):
    group_name: NotRequired["capo_resource_groups.types.group_name.GroupName"]
    """<important> <p> <i> <b>Deprecated - don't use this parameter. Use the <code>Group</code> request field instead.</b> </i> </p> </important>"""
    group: NotRequired["capo_resource_groups.types.group_string_v2.GroupStringV2"]
    """<p>The name or the Amazon resource name (ARN) of the resource group. </p>"""
    filters: NotRequired[
        "capo_resource_groups.types.resource_filter_list.ResourceFilterList"
    ]
    """<p>Filters, formatted as <a>ResourceFilter</a> objects, that you want to apply to a <code>ListGroupResources</code> operation. Filters the results to include only those of the specified resource types.</p> <ul> <li> <p> <code>resource-type</code> - Filter resources by their type. Specify up to five resource types in the format <code>AWS::ServiceCode::ResourceType</code>. For example, <code>AWS::EC2::Instance</code>, or <code>AWS::S3::Bucket</code>. </p> </li> </ul> <p>When you specify a <code>resource-type</code> filter for <code>ListGroupResources</code>, Resource Groups validates your filter resource types against the types that are defined in the query associated with the group. For example, if a group contains only S3 buckets because its query specifies only that resource type, but your <code>resource-type</code> filter includes EC2 instances, AWS Resource Groups does not filter for EC2 instances. In this case, a <code>ListGroupResources</code> request returns a <code>BadRequestException</code> error with a message similar to the following:</p> <p> <code>The resource types specified as filters in the request are not valid.</code> </p> <p>The error includes a list of resource types that failed the validation because they are not part of the query associated with the group. This validation doesn't occur when the group query specifies <code>AWS::AllSupported</code>, because a group based on such a query can contain any of the allowed resource types for the query type (tag-based or Amazon CloudFront stack-based queries).</p>"""
    max_results: NotRequired["capo_resource_groups.types.max_results.MaxResults"]
    """<p>The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>"""
    next_token: NotRequired["capo_resource_groups.types.next_token.NextToken"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value provided by a previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupResourcesInput) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "group" in value:
        out["Group"] = value["group"]
    if "filters" in value:
        import capo_resource_groups.types.resource_filter_list

        out["Filters"] = capo_resource_groups.types.resource_filter_list.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListGroupResourcesInput:
    out: ListGroupResourcesInput = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "Group" in data:
        out["group"] = data["Group"]
    if "Filters" in data:
        import capo_resource_groups.types.resource_filter_list

        out["filters"] = (
            capo_resource_groups.types.resource_filter_list.deserialize_json(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
