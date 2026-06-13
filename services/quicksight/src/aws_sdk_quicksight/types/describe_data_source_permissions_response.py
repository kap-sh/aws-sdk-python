"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDataSourcePermissionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_id
    import aws_sdk_quicksight.types.resource_permission_list
    import aws_sdk_quicksight.types.status_code
    import aws_sdk_quicksight.types.string


class DescribeDataSourcePermissionsResponse(TypedDict):
    data_source_arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the data source.</p>"""
    data_source_id: NotRequired["aws_sdk_quicksight.types.resource_id.ResourceId"]
    """<p>The ID of the data source. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    permissions: NotRequired[
        "aws_sdk_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>A list of resource permissions on the data source.</p>"""
    request_id: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDataSourcePermissionsResponse) -> dict:
    out: dict = {}
    if "data_source_arn" in value:
        out["DataSourceArn"] = value["data_source_arn"]
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    if "permissions" in value:
        import aws_sdk_quicksight.types.resource_permission_list

        out["Permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeDataSourcePermissionsResponse:
    out: DescribeDataSourcePermissionsResponse = {}  # type: ignore[typeddict-item]
    if "DataSourceArn" in data:
        out["data_source_arn"] = data["DataSourceArn"]
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    if "Permissions" in data:
        import aws_sdk_quicksight.types.resource_permission_list

        out["permissions"] = (
            aws_sdk_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
