"""Generated from Smithy shape ``com.amazonaws.quicksight#ActionConnectorError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.action_connector_error_type


class ActionConnectorError(TypedDict, closed=True):
    message: NotRequired["str"]
    """<p>The error message describing what went wrong with the action connector.</p>"""
    type: NotRequired[
        "aws_sdk_quicksight.types.action_connector_error_type.ActionConnectorErrorType"
    ]
    """<p>The type or category of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionConnectorError) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "type" in value:
        import aws_sdk_quicksight.types.action_connector_error_type

        out["Type"] = (
            aws_sdk_quicksight.types.action_connector_error_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ActionConnectorError:
    out: ActionConnectorError = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Type" in data:
        import aws_sdk_quicksight.types.action_connector_error_type

        out["type"] = (
            aws_sdk_quicksight.types.action_connector_error_type.deserialize_json(
                data["Type"]
            )
        )
    return out
