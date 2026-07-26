"""Generated from Smithy shape ``com.amazonaws.resourcegroups#ListGroupsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_groups.types.group_filter_list
    import capo_resource_groups.types.max_results
    import capo_resource_groups.types.next_token


class ListGroupsInput(TypedDict, closed=True):
    filters: NotRequired["capo_resource_groups.types.group_filter_list.GroupFilterList"]
    """<p>Filters, formatted as <a>GroupFilter</a> objects, that you want to apply to a <code>ListGroups</code> operation.</p> <ul> <li> <p> <code>resource-type</code> - Filter the results to include only those resource groups that have the specified resource type in their <code>ResourceTypeFilter</code>. For example, <code>AWS::EC2::Instance</code> would return any resource group with a <code>ResourceTypeFilter</code> that includes <code>AWS::EC2::Instance</code>.</p> </li> <li> <p> <code>configuration-type</code> - Filter the results to include only those groups that have the specified configuration types attached. The current supported values are:</p> <ul> <li> <p> <code>AWS::ResourceGroups::ApplicationGroup</code> </p> </li> <li> <p> <code>AWS::AppRegistry::Application</code> </p> </li> <li> <p> <code>AWS::AppRegistry::ApplicationResourceGroup</code> </p> </li> <li> <p> <code>AWS::CloudFormation::Stack</code> </p> </li> <li> <p> <code>AWS::EC2::CapacityReservationPool</code> </p> </li> <li> <p> <code>AWS::EC2::HostManagement</code> </p> </li> <li> <p> <code>AWS::NetworkFirewall::RuleGroup</code> </p> </li> </ul> </li> </ul>"""
    max_results: NotRequired["capo_resource_groups.types.max_results.MaxResults"]
    """<p>The total number of results that you want included on each page of the response. If you do not include this parameter, it defaults to a value that is specific to the operation. If additional items exist beyond the maximum you specify, the <code>NextToken</code> response element is present and has a value (is not null). Include that value as the <code>NextToken</code> request parameter in the next call to the operation to get the next part of the results. Note that the service might return fewer results than the maximum even when there are more results available. You should check <code>NextToken</code> after every operation to ensure that you receive all of the results.</p>"""
    next_token: NotRequired["capo_resource_groups.types.next_token.NextToken"]
    """<p>The parameter for receiving additional results if you receive a <code>NextToken</code> response in a previous request. A <code>NextToken</code> response indicates that more output is available. Set this parameter to the value provided by a previous call's <code>NextToken</code> response to indicate where the output should continue from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListGroupsInput) -> dict:
    out: dict = {}
    if "filters" in value:
        import capo_resource_groups.types.group_filter_list

        out["Filters"] = capo_resource_groups.types.group_filter_list.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> ListGroupsInput:
    out: ListGroupsInput = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import capo_resource_groups.types.group_filter_list

        out["filters"] = capo_resource_groups.types.group_filter_list.deserialize_json(
            data["Filters"]
        )
    return out
