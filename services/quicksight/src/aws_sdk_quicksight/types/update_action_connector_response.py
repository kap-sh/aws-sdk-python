"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateActionConnectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_status
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.status_code


class UpdateActionConnectorResponse(TypedDict):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the updated action connector.</p>"""
    action_connector_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>The unique identifier of the updated action connector.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    update_status: NotRequired[
        "aws_sdk_quicksight.types.resource_status.ResourceStatus"
    ]
    """<p>The status of the update operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status code of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateActionConnectorResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "action_connector_id" in value:
        out["ActionConnectorId"] = value["action_connector_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    if "update_status" in value:
        import aws_sdk_quicksight.types.resource_status

        out["UpdateStatus"] = aws_sdk_quicksight.types.resource_status.serialize_json(
            value["update_status"]
        )
    return out


def deserialize_json(data: dict) -> UpdateActionConnectorResponse:
    out: UpdateActionConnectorResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "ActionConnectorId" in data:
        out["action_connector_id"] = data["ActionConnectorId"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    if "UpdateStatus" in data:
        import aws_sdk_quicksight.types.resource_status

        out["update_status"] = (
            aws_sdk_quicksight.types.resource_status.deserialize_json(
                data["UpdateStatus"]
            )
        )
    return out
