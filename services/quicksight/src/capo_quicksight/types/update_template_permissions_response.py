"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateTemplatePermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.update_resource_permission_list


class UpdateTemplatePermissionsResponse(TypedDict, closed=True):
    template_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID for the template.</p>"""
    template_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the template.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.update_resource_permission_list.UpdateResourcePermissionList"
    ]
    """<p>A list of resource permissions to be set on the template.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTemplatePermissionsResponse) -> dict:
    out: dict = {}
    if "template_id" in value:
        out["TemplateId"] = value["template_id"]
    if "template_arn" in value:
        out["TemplateArn"] = value["template_arn"]
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


def deserialize_json(data: dict) -> UpdateTemplatePermissionsResponse:
    out: UpdateTemplatePermissionsResponse = {}  # type: ignore[typeddict-item]
    if "TemplateId" in data:
        out["template_id"] = data["TemplateId"]
    if "TemplateArn" in data:
        out["template_arn"] = data["TemplateArn"]
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
