"""Generated from Smithy shape ``com.amazonaws.licensemanagerusersubscriptions#ListUserAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager_user_subscriptions.types.instance_user_summary_list


class ListUserAssociationsResponse(TypedDict, closed=True):
    instance_user_summaries: NotRequired[
        "capo_license_manager_user_subscriptions.types.instance_user_summary_list.InstanceUserSummaryList"
    ]
    """<p>Metadata that describes the list user association operation.</p>"""
    next_token: NotRequired["str"]
    """<p>The next token used for paginated responses. When this field isn't empty, there are additional elements that the service hasn't included in this request. Use this token with the next request to retrieve additional objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListUserAssociationsResponse) -> dict:
    out: dict = {}
    if "instance_user_summaries" in value:
        import capo_license_manager_user_subscriptions.types.instance_user_summary_list

        out["InstanceUserSummaries"] = (
            capo_license_manager_user_subscriptions.types.instance_user_summary_list.serialize_json(
                value["instance_user_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListUserAssociationsResponse:
    out: ListUserAssociationsResponse = {}  # type: ignore[typeddict-item]
    if "InstanceUserSummaries" in data:
        import capo_license_manager_user_subscriptions.types.instance_user_summary_list

        out["instance_user_summaries"] = (
            capo_license_manager_user_subscriptions.types.instance_user_summary_list.deserialize_json(
                data["InstanceUserSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
