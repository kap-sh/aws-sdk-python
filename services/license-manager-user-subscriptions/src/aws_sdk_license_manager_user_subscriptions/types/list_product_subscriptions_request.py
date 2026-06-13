"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ListProductSubscriptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.box_integer
    import aws_sdk_license_manager_user_subscriptions.types.filter_list
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider


class ListProductSubscriptionsRequest(TypedDict):
    product: NotRequired["str"]
    """<p>The name of the user-based subscription product.</p> <p>Valid values: <code>VISUAL_STUDIO_ENTERPRISE</code> | <code>VISUAL_STUDIO_PROFESSIONAL</code> | <code>OFFICE_PROFESSIONAL_PLUS</code> | <code>REMOTE_DESKTOP_SERVICES</code> </p>"""
    identity_provider: "aws_sdk_license_manager_user_subscriptions.types.identity_provider.IdentityProvider"
    """<p>An object that specifies details for the identity provider.</p>"""
    max_results: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.box_integer.BoxInteger"
    ]
    """<p>The maximum number of results to return from a single request.</p>"""
    filters: NotRequired[
        "aws_sdk_license_manager_user_subscriptions.types.filter_list.FilterList"
    ]
    """<p>You can use the following filters to streamline results:</p> <ul> <li> <p>Status</p> </li> <li> <p>Username</p> </li> <li> <p>Domain</p> </li> </ul>"""
    next_token: NotRequired["str"]
    """<p>A token to specify where to start paginating. This is the nextToken from a previously truncated response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProductSubscriptionsRequest) -> dict:
    out: dict = {}
    if "product" in value:
        out["Product"] = value["product"]
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider

    out["IdentityProvider"] = (
        aws_sdk_license_manager_user_subscriptions.types.identity_provider.serialize_json(
            value["identity_provider"]
        )
    )
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


def deserialize_json(data: dict) -> ListProductSubscriptionsRequest:
    out: ListProductSubscriptionsRequest = {}  # type: ignore[typeddict-item]
    if "Product" in data:
        out["product"] = data["Product"]
    if "IdentityProvider" in data:
        import aws_sdk_license_manager_user_subscriptions.types.identity_provider

        out["identity_provider"] = (
            aws_sdk_license_manager_user_subscriptions.types.identity_provider.deserialize_json(
                data["IdentityProvider"]
            )
        )
    else:
        raise DeserializationError(
            "ListProductSubscriptionsRequest.identity_provider required"
        )
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
