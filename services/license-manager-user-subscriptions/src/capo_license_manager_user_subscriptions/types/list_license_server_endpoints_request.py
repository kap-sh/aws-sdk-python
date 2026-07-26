"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ListLicenseServerEndpointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.box_integer
    import capo_license_manager_user_subscriptions.types.filter_list


class ListLicenseServerEndpointsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_license_manager_user_subscriptions.types.box_integer.BoxInteger"
    ]
    """<p>The maximum number of results to return from a single request.</p>"""
    filters: NotRequired[
        "capo_license_manager_user_subscriptions.types.filter_list.FilterList"
    ]
    """<p>You can use the following filters to streamline results:</p> <ul> <li> <p>IdentityProviderArn</p> </li> </ul>"""
    next_token: NotRequired["str"]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLicenseServerEndpointsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import capo_license_manager_user_subscriptions.types.filter_list

        out["Filters"] = (
            capo_license_manager_user_subscriptions.types.filter_list.serialize_json(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLicenseServerEndpointsRequest:
    out: ListLicenseServerEndpointsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Filters" in data:
        import capo_license_manager_user_subscriptions.types.filter_list

        out["filters"] = (
            capo_license_manager_user_subscriptions.types.filter_list.deserialize_json(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
