"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ListUserAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_license_manager_user_subscriptions.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager_user_subscriptions.types.box_integer
    import aws_sdk_license_manager_user_subscriptions.types.filter_list
    import aws_sdk_license_manager_user_subscriptions.types.identity_provider


class ListUserAssociationsRequest(TypedDict, closed=True):
    instance_id: "str"
    """<p>The ID of the EC2 instance, which provides user-based subscriptions.</p>"""
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
def serialize_json(value: ListUserAssociationsRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
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


def deserialize_json(data: dict) -> ListUserAssociationsRequest:
    out: ListUserAssociationsRequest = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("ListUserAssociationsRequest.instance_id required")
    if "IdentityProvider" in data:
        import aws_sdk_license_manager_user_subscriptions.types.identity_provider

        out["identity_provider"] = (
            aws_sdk_license_manager_user_subscriptions.types.identity_provider.deserialize_json(
                data["IdentityProvider"]
            )
        )
    else:
        raise DeserializationError(
            "ListUserAssociationsRequest.identity_provider required"
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
