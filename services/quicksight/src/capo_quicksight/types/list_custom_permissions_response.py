"""Generated from Smithy shape ``com.amazonaws.quicksight#ListCustomPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.custom_permissions_list
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class ListCustomPermissionsResponse(TypedDict, closed=True):
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    custom_permissions_list: NotRequired[
        "capo_quicksight.types.custom_permissions_list.CustomPermissionsList"
    ]
    """<p>A list of custom permissions profiles.</p>"""
    next_token: NotRequired["capo_quicksight.types.string.String"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomPermissionsResponse) -> dict:
    out: dict = {}
    if "custom_permissions_list" in value:
        import capo_quicksight.types.custom_permissions_list

        out["CustomPermissionsList"] = (
            capo_quicksight.types.custom_permissions_list.serialize_json(
                value["custom_permissions_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> ListCustomPermissionsResponse:
    out: ListCustomPermissionsResponse = {}  # type: ignore[typeddict-item]
    if "CustomPermissionsList" in data:
        import capo_quicksight.types.custom_permissions_list

        out["custom_permissions_list"] = (
            capo_quicksight.types.custom_permissions_list.deserialize_json(
                data["CustomPermissionsList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
