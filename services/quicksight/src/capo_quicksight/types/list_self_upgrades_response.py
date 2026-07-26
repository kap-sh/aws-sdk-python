"""Generated from Smithy shape ``com.amazonaws.quicksight#ListSelfUpgradesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.self_upgrade_request_detail_list
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class ListSelfUpgradesResponse(TypedDict, closed=True):
    self_upgrade_request_details: NotRequired[
        "capo_quicksight.types.self_upgrade_request_detail_list.SelfUpgradeRequestDetailList"
    ]
    """<p>A list of self-upgrade request details.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSelfUpgradesResponse) -> dict:
    out: dict = {}
    if "self_upgrade_request_details" in value:
        import capo_quicksight.types.self_upgrade_request_detail_list

        out["SelfUpgradeRequestDetails"] = (
            capo_quicksight.types.self_upgrade_request_detail_list.serialize_json(
                value["self_upgrade_request_details"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListSelfUpgradesResponse:
    out: ListSelfUpgradesResponse = {}  # type: ignore[typeddict-item]
    if "SelfUpgradeRequestDetails" in data:
        import capo_quicksight.types.self_upgrade_request_detail_list

        out["self_upgrade_request_details"] = (
            capo_quicksight.types.self_upgrade_request_detail_list.deserialize_json(
                data["SelfUpgradeRequestDetails"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
