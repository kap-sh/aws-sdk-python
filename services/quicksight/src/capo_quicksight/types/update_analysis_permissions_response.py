"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAnalysisPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string
    import capo_quicksight.types.update_resource_permission_list


class UpdateAnalysisPermissionsResponse(TypedDict, closed=True):
    analysis_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the analysis that you updated.</p>"""
    analysis_id: NotRequired[
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the analysis that you updated permissions for.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.update_resource_permission_list.UpdateResourcePermissionList"
    ]
    """<p>A structure that describes the principals and the resource-level permissions on an analysis.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAnalysisPermissionsResponse) -> dict:
    out: dict = {}
    if "analysis_arn" in value:
        out["AnalysisArn"] = value["analysis_arn"]
    if "analysis_id" in value:
        out["AnalysisId"] = value["analysis_id"]
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


def deserialize_json(data: dict) -> UpdateAnalysisPermissionsResponse:
    out: UpdateAnalysisPermissionsResponse = {}  # type: ignore[typeddict-item]
    if "AnalysisArn" in data:
        out["analysis_arn"] = data["AnalysisArn"]
    if "AnalysisId" in data:
        out["analysis_id"] = data["AnalysisId"]
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
