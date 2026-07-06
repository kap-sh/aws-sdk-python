"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateActionConnectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.resource_status
    import aws_sdk_quicksight.types.status_code


class CreateActionConnectorResponse(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the created action connector.</p>"""
    creation_status: NotRequired[
        "aws_sdk_quicksight.types.resource_status.ResourceStatus"
    ]
    """<p>The creation status of the action connector.</p>"""
    action_connector_id: NotRequired["str"]
    """<p>The unique identifier of the created action connector.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status code of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateActionConnectorResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "creation_status" in value:
        import aws_sdk_quicksight.types.resource_status

        out["CreationStatus"] = aws_sdk_quicksight.types.resource_status.serialize_json(
            value["creation_status"]
        )
    if "action_connector_id" in value:
        out["ActionConnectorId"] = value["action_connector_id"]
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateActionConnectorResponse:
    out: CreateActionConnectorResponse = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreationStatus" in data:
        import aws_sdk_quicksight.types.resource_status

        out["creation_status"] = (
            aws_sdk_quicksight.types.resource_status.deserialize_json(
                data["CreationStatus"]
            )
        )
    if "ActionConnectorId" in data:
        out["action_connector_id"] = data["ActionConnectorId"]
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
