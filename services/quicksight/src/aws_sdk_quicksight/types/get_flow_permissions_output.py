"""Generated from Smithy shape ``com.amazonaws.quicksight#GetFlowPermissionsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.flow_id
    import aws_sdk_quicksight.types.permissions_list
    import aws_sdk_quicksight.types.status_code


class GetFlowPermissionsOutput(TypedDict):
    arn: "aws_sdk_quicksight.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the flow you are getting permissions against.</p>"""
    flow_id: "aws_sdk_quicksight.types.flow_id.FlowId"
    """<p>The unique identifier of the flow with permissions.</p>"""
    permissions: "aws_sdk_quicksight.types.permissions_list.PermissionsList"
    """<p>A structure that contains the permissions for the flow.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFlowPermissionsOutput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["FlowId"] = value["flow_id"]
    import aws_sdk_quicksight.types.permissions_list

    out["Permissions"] = aws_sdk_quicksight.types.permissions_list.serialize_json(
        value["permissions"]
    )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> GetFlowPermissionsOutput:
    out: GetFlowPermissionsOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("GetFlowPermissionsOutput.arn required")
    if "FlowId" in data:
        out["flow_id"] = data["FlowId"]
    else:
        raise DeserializationError("GetFlowPermissionsOutput.flow_id required")
    if "Permissions" in data:
        import aws_sdk_quicksight.types.permissions_list

        out["permissions"] = aws_sdk_quicksight.types.permissions_list.deserialize_json(
            data["Permissions"]
        )
    else:
        raise DeserializationError("GetFlowPermissionsOutput.permissions required")
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
