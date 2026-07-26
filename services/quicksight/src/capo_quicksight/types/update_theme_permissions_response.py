"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateThemePermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.update_resource_permission_list


class UpdateThemePermissionsResponse(TypedDict, closed=True):
    theme_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID for the theme.</p>"""
    theme_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the theme.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.update_resource_permission_list.UpdateResourcePermissionList"
    ]
    """<p>The resulting list of resource permissions for the theme.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateThemePermissionsResponse) -> dict:
    out: dict = {}
    if "theme_id" in value:
        out["ThemeId"] = value["theme_id"]
    if "theme_arn" in value:
        out["ThemeArn"] = value["theme_arn"]
    if "permissions" in value:
        import capo_quicksight.types.update_resource_permission_list

        out["Permissions"] = (
            capo_quicksight.types.update_resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateThemePermissionsResponse:
    out: UpdateThemePermissionsResponse = {}  # type: ignore[typeddict-item]
    if "ThemeId" in data:
        out["theme_id"] = data["ThemeId"]
    if "ThemeArn" in data:
        out["theme_arn"] = data["ThemeArn"]
    if "Permissions" in data:
        import capo_quicksight.types.update_resource_permission_list

        out["permissions"] = (
            capo_quicksight.types.update_resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
