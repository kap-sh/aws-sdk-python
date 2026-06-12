"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#ListLinuxSubscriptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.box_integer
    import aws_sdk_license_manager_linux_subscriptions.types.filter_list


class ListLinuxSubscriptionsRequest(TypedDict):
    filters: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.filter_list.FilterList"
    ]
    """<p>An array of structures that you can use to filter the results to those that match one or more sets of key-value pairs that you specify. For example, you can filter by the name of <code>Subscription</code> with an optional operator to see subscriptions that match, partially match, or don't match a certain subscription's name.</p> <p>The valid names for this filter are:</p> <ul> <li> <p> <code>Subscription</code> </p> </li> </ul> <p>The valid Operators for this filter are:</p> <ul> <li> <p> <code>contains</code> </p> </li> <li> <p> <code>equals</code> </p> </li> <li> <p> <code>Notequal</code> </p> </li> </ul>"""
    max_results: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.box_integer.BoxInteger"
    ]
    """<p>The maximum items to return in a request.</p>"""
    next_token: NotRequired["str"]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLinuxSubscriptionsRequest) -> dict:
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


def deserialize_json(data: dict) -> ListLinuxSubscriptionsRequest:
    out: ListLinuxSubscriptionsRequest = {}  # type: ignore[typeddict-item]
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
