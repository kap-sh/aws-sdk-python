"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeAnalysisPermissionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.update_resource_permission_list


class DescribeAnalysisPermissionsResponse(TypedDict):
    analysis_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID of the analysis whose permissions you're describing.</p>"""
    analysis_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the analysis whose permissions you're describing.</p>"""
    permissions: NotRequired[
        "aws_sdk_quicksight.types.update_resource_permission_list.UpdateResourcePermissionList"
    ]
    """<p>A structure that describes the principals and the resource-level permissions on an analysis.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAnalysisPermissionsResponse) -> dict:
    out: dict = {}
    if "analysis_id" in value:
        out["AnalysisId"] = value["analysis_id"]
    if "analysis_arn" in value:
        out["AnalysisArn"] = value["analysis_arn"]
    if "permissions" in value:
        import aws_sdk_quicksight.types.update_resource_permission_list

        out["Permissions"] = (
            aws_sdk_quicksight.types.update_resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeAnalysisPermissionsResponse:
    out: DescribeAnalysisPermissionsResponse = {}  # type: ignore[typeddict-item]
    if "AnalysisId" in data:
        out["analysis_id"] = data["AnalysisId"]
    if "AnalysisArn" in data:
        out["analysis_arn"] = data["AnalysisArn"]
    if "Permissions" in data:
        import aws_sdk_quicksight.types.update_resource_permission_list

        out["permissions"] = (
            aws_sdk_quicksight.types.update_resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
