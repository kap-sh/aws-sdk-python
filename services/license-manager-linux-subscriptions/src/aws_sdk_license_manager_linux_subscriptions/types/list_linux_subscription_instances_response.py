"""Generated from Smithy shape ``com.amazonaws.licensemanagerlinuxsubscriptions#ListLinuxSubscriptionInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager_linux_subscriptions.types.instance_list


class ListLinuxSubscriptionInstancesResponse(TypedDict, closed=True):
    instances: NotRequired[
        "aws_sdk_license_manager_linux_subscriptions.types.instance_list.InstanceList"
    ]
    """<p>An array that contains instance objects.</p>"""
    next_token: NotRequired["str"]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLinuxSubscriptionInstancesResponse) -> dict:
    out: dict = {}
    if "instances" in value:
        import aws_sdk_license_manager_linux_subscriptions.types.instance_list

        out["Instances"] = (
            aws_sdk_license_manager_linux_subscriptions.types.instance_list.serialize_json(
                value["instances"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLinuxSubscriptionInstancesResponse:
    out: ListLinuxSubscriptionInstancesResponse = {}  # type: ignore[typeddict-item]
    if "Instances" in data:
        import aws_sdk_license_manager_linux_subscriptions.types.instance_list

        out["instances"] = (
            aws_sdk_license_manager_linux_subscriptions.types.instance_list.deserialize_json(
                data["Instances"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
