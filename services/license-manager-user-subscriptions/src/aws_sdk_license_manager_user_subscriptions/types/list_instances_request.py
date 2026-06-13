"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ListInstancesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.box_integer
    import aws_sdk_license_manager_user_subscriptions.types.filter_list


class ListInstancesRequest(TypedDict):
    max_results: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.box_integer.BoxInteger"
    ]
    """<p>The maximum number of results to return from a single request.</p>"""
    next_token: NotRequired["str"]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""
    filters: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.filter_list.FilterList"
    ]
    """<p>You can use the following filters to streamline results:</p> <ul> <li> <p>Status</p> </li> <li> <p>InstanceId</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInstancesRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_license_manager_user_subscriptions.types.filter_list

        out["Filters"] = (
            aws_sdk_license_manager_user_subscriptions.types.filter_list.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListInstancesRequest:
    out: ListInstancesRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import aws_sdk_license_manager_user_subscriptions.types.filter_list

        out["filters"] = (
            aws_sdk_license_manager_user_subscriptions.types.filter_list.deserialize_json(
                data["Filters"]
            )
        )
    return out
