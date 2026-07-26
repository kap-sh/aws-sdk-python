"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ListInstancesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.instance_summary_list


class ListInstancesResponse(TypedDict, closed=True):
    instance_summaries: NotRequired[
        "capo_license_manager_user_subscriptions.types.instance_summary_list.InstanceSummaryList"
    ]
    """<p>An array of <code>InstanceSummary</code> resources that contain details about the instances that provide user-based subscriptions and also meet the request criteria.</p>"""
    next_token: NotRequired["str"]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInstancesResponse) -> dict:
    out: dict = {}
    if "instance_summaries" in value:
        import capo_license_manager_user_subscriptions.types.instance_summary_list

        out["InstanceSummaries"] = (
            capo_license_manager_user_subscriptions.types.instance_summary_list.serialize_json(
                value["instance_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInstancesResponse:
    out: ListInstancesResponse = {}  # type: ignore[typeddict-item]
    if "InstanceSummaries" in data:
        import capo_license_manager_user_subscriptions.types.instance_summary_list

        out["instance_summaries"] = (
            capo_license_manager_user_subscriptions.types.instance_summary_list.deserialize_json(
                data["InstanceSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
