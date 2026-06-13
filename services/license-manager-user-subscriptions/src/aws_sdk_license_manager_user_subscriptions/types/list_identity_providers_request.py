"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ListIdentityProvidersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.box_integer
    import aws_sdk_license_manager_user_subscriptions.types.filter_list


class ListIdentityProvidersRequest(TypedDict):
    max_results: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.box_integer.BoxInteger"
    ]
    """<p>The maximum number of results to return from a single request.</p>"""
    filters: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.filter_list.FilterList"
    ]
    """<p>You can use the following filters to streamline results:</p> <ul> <li> <p>Product</p> </li> <li> <p>DirectoryId</p> </li> </ul>"""
    next_token: NotRequired["str"]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdentityProvidersRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import aws_sdk_license_manager_user_subscriptions.types.filter_list

        out["Filters"] = (
            aws_sdk_license_manager_user_subscriptions.types.filter_list.serialize_json(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListIdentityProvidersRequest:
    out: ListIdentityProvidersRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Filters" in data:
        import aws_sdk_license_manager_user_subscriptions.types.filter_list

        out["filters"] = (
            aws_sdk_license_manager_user_subscriptions.types.filter_list.deserialize_json(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
