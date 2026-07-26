"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeDataSetPermissionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.resource_id
    import capo_quicksight.types.resource_permission_list
    import capo_quicksight.types.status_code
    import capo_quicksight.types.string


class DescribeDataSetPermissionsResponse(TypedDict, closed=True):
    data_set_arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset.</p>"""
    data_set_id: NotRequired["capo_quicksight.types.resource_id.ResourceId"]
    """<p>The ID for the dataset that you want to describe. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.</p>"""
    permissions: NotRequired[
        "capo_quicksight.types.resource_permission_list.ResourcePermissionList"
    ]
    """<p>A list of resource permissions on the dataset.</p>"""
    request_id: NotRequired["capo_quicksight.types.string.String"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "capo_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeDataSetPermissionsResponse) -> dict:
    out: dict = {}
    if "data_set_arn" in value:
        out["DataSetArn"] = value["data_set_arn"]
    if "data_set_id" in value:
        out["DataSetId"] = value["data_set_id"]
    if "permissions" in value:
        import capo_quicksight.types.resource_permission_list

        out["Permissions"] = (
            capo_quicksight.types.resource_permission_list.serialize_json(
                value["permissions"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeDataSetPermissionsResponse:
    out: DescribeDataSetPermissionsResponse = {}  # type: ignore[typeddict-item]
    if "DataSetArn" in data:
        out["data_set_arn"] = data["DataSetArn"]
    if "DataSetId" in data:
        out["data_set_id"] = data["DataSetId"]
    if "Permissions" in data:
        import capo_quicksight.types.resource_permission_list

        out["permissions"] = (
            capo_quicksight.types.resource_permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
