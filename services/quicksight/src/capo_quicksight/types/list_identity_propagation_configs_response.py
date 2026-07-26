"""Generated from Smithy shape ``com.amazonaws.quicksight#ListIdentityPropagationConfigsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.authorized_targets_by_services
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class ListIdentityPropagationConfigsResponse(TypedDict, closed=True):
    services: NotRequired[
        "capo_quicksight.types.authorized_targets_by_services.AuthorizedTargetsByServices"
    ]
    """<p>A list of services and their authorized targets that the Quick Sight IAM Identity Center application can access.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIdentityPropagationConfigsResponse) -> dict:
    out: dict = {}
    if "services" in value:
        import capo_quicksight.types.authorized_targets_by_services

        out["Services"] = (
            capo_quicksight.types.authorized_targets_by_services.serialize_json(
                value["services"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListIdentityPropagationConfigsResponse:
    out: ListIdentityPropagationConfigsResponse = {}  # type: ignore[typeddict-item]
    if "Services" in data:
        import capo_quicksight.types.authorized_targets_by_services

        out["services"] = (
            capo_quicksight.types.authorized_targets_by_services.deserialize_json(
                data["Services"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
