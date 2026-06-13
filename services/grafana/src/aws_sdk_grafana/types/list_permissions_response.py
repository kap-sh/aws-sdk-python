"""Generated from Smithy shape ``com.amazonaws.grafana#ListPermissionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.pagination_token
    import aws_sdk_grafana.types.permission_entry_list


class ListPermissionsResponse(TypedDict):
    next_token: NotRequired["aws_sdk_grafana.types.pagination_token.PaginationToken"]
    """<p>The token to use in a subsequent <code>ListPermissions</code> operation to return the next set of results.</p>"""
    permissions: "aws_sdk_grafana.types.permission_entry_list.PermissionEntryList"
    """<p>The permissions returned by the operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPermissionsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_grafana.types.permission_entry_list

    out["permissions"] = aws_sdk_grafana.types.permission_entry_list.serialize_json(
        value["permissions"]
    )
    return out


def deserialize_json(data: dict) -> ListPermissionsResponse:
    out: ListPermissionsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "permissions" in data:
        import aws_sdk_grafana.types.permission_entry_list

        out["permissions"] = (
            aws_sdk_grafana.types.permission_entry_list.deserialize_json(
                data["permissions"]
            )
        )
    else:
        raise DeserializationError("ListPermissionsResponse.permissions required")
    return out
