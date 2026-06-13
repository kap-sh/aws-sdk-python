"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateDashboardResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_status
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class UpdateDashboardResponse(TypedDict):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    version_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The ARN of the dashboard, including the version number.</p>"""
    dashboard_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The ID for the dashboard.</p>"""
    creation_status: NotRequired[
        "aws_sdk_quicksight.types.resource_status.ResourceStatus"
    ]
    """<p>The creation status of the request.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDashboardResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "version_arn" in value:
        out["VersionArn"] = value["version_arn"]
    if "dashboard_id" in value:
        out["DashboardId"] = value["dashboard_id"]
    if "creation_status" in value:
        import aws_sdk_quicksight.types.resource_status

        out["CreationStatus"] = aws_sdk_quicksight.types.resource_status.serialize_json(
            value["creation_status"]
        )
    out["Status"] = value.get("status", 0)
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> UpdateDashboardResponse:
    out: UpdateDashboardResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "VersionArn" in data:
        out["version_arn"] = data["VersionArn"]
    if "DashboardId" in data:
        out["dashboard_id"] = data["DashboardId"]
    if "CreationStatus" in data:
        import aws_sdk_quicksight.types.resource_status

        out["creation_status"] = (
            aws_sdk_quicksight.types.resource_status.deserialize_json(
                data["CreationStatus"]
            )
        )
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        out["status"] = 0
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
