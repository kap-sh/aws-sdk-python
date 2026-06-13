"""Generated from Smithy shape ``com.amazonaws.quicksight#DescribeActionConnectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.action_connector
    import aws_sdk_quicksight.types.status_code


class DescribeActionConnectorResponse(TypedDict):
    action_connector: NotRequired[
        "aws_sdk_quicksight.types.action_connector.ActionConnector"
    ]
    """<p>The detailed information about the action connector, including its configuration and current state.</p>"""
    request_id: NotRequired["str"]
    """<p>The Amazon Web Services request ID for this operation.</p>"""
    status: "aws_sdk_quicksight.types.status_code.StatusCode"
    """<p>The HTTP status code of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeActionConnectorResponse) -> dict:
    out: dict = {}
    if "action_connector" in value:
        import aws_sdk_quicksight.types.action_connector

        out["ActionConnector"] = (
            aws_sdk_quicksight.types.action_connector.serialize_json(
                value["action_connector"]
            )
        )
    if "request_id" in value:
        out["RequestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> DescribeActionConnectorResponse:
    out: DescribeActionConnectorResponse = {}  # type: ignore[typeddict-item]
    if "ActionConnector" in data:
        import aws_sdk_quicksight.types.action_connector

        out["action_connector"] = (
            aws_sdk_quicksight.types.action_connector.deserialize_json(
                data["ActionConnector"]
            )
        )
    if "RequestId" in data:
        out["request_id"] = data["RequestId"]
    return out
