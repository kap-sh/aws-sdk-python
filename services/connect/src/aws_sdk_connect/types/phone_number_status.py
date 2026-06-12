"""Generated from Smithy shape ``com.amazonaws.connect#PhoneNumberStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.phone_number_workflow_message
    import aws_sdk_connect.types.phone_number_workflow_status


class PhoneNumberStatus(TypedDict):
    status: NotRequired[
        "aws_sdk_connect.types.phone_number_workflow_status.PhoneNumberWorkflowStatus"
    ]
    """<p>The status.</p>"""
    message: NotRequired[
        "aws_sdk_connect.types.phone_number_workflow_message.PhoneNumberWorkflowMessage"
    ]
    """<p>The status message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PhoneNumberStatus) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_connect.types.phone_number_workflow_status

        out["Status"] = (
            aws_sdk_connect.types.phone_number_workflow_status.serialize_json(
                value["status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> PhoneNumberStatus:
    out: PhoneNumberStatus = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_connect.types.phone_number_workflow_status

        out["status"] = (
            aws_sdk_connect.types.phone_number_workflow_status.deserialize_json(
                data["Status"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
