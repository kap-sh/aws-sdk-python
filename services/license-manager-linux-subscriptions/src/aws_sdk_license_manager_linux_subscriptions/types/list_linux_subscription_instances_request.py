"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#ListLinuxSubscriptionInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.box_integer
    import aws_sdk_license_manager_linux_subscriptions.types.filter_list


class ListLinuxSubscriptionInstancesRequest(TypedDict):
    filters: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.filter_list.FilterList"
    ]
    """<p>An array of structures that you can use to filter the results by your specified criteria. For example, you can specify <code>Region</code> in the <code>Name</code>, with the <code>contains</code> operator to list all subscriptions that match a partial string in the <code>Value</code>, such as <code>us-west</code>.</p> <p>For each filter, you can specify one of the following values for the <code>Name</code> key to streamline results:</p> <ul> <li> <p> <code>AccountID</code> </p> </li> <li> <p> <code>AmiID</code> </p> </li> <li> <p> <code>DualSubscription</code> </p> </li> <li> <p> <code>InstanceID</code> </p> </li> <li> <p> <code>InstanceType</code> </p> </li> <li> <p> <code>ProductCode</code> </p> </li> <li> <p> <code>Region</code> </p> </li> <li> <p> <code>Status</code> </p> </li> <li> <p> <code>UsageOperation</code> </p> </li> </ul> <p>For each filter, you can use one of the following <code>Operator</code> values to define the behavior of the filter:</p> <ul> <li> <p> <code>contains</code> </p> </li> <li> <p> <code>equals</code> </p> </li> <li> <p> <code>Notequal</code> </p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.box_integer.BoxInteger"
    ]
    """<p>The maximum items to return in a request.</p>"""
    next_token: NotRequired["str"]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLinuxSubscriptionInstancesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_license_manager_linux_subscriptions.types.filter_list

        out["Filters"] = (
            aws_sdk_license_manager_linux_subscriptions.types.filter_list.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLinuxSubscriptionInstancesRequest:
    out: ListLinuxSubscriptionInstancesRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_license_manager_linux_subscriptions.types.filter_list

        out["filters"] = (
            aws_sdk_license_manager_linux_subscriptions.types.filter_list.deserialize_json(
                data["Filters"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
