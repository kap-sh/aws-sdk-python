"""Generated from Smithy shape ``com.amazonaws.qbusiness#AttachmentsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.attachments_control_mode


class AttachmentsConfiguration(TypedDict):
    attachments_control_mode: (
        "aws_sdk_qbusiness.types.attachments_control_mode.AttachmentsControlMode"
    )
    """<p>Status information about whether file upload functionality is activated or deactivated for your end user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttachmentsConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.attachments_control_mode

    out["attachmentsControlMode"] = (
        aws_sdk_qbusiness.types.attachments_control_mode.serialize_json(
            value["attachments_control_mode"]
        )
    )
    return out


def deserialize_json(data: dict) -> AttachmentsConfiguration:
    out: AttachmentsConfiguration = {}  # type: ignore[typeddict-item]
    if "attachmentsControlMode" in data:
        import aws_sdk_qbusiness.types.attachments_control_mode

        out["attachments_control_mode"] = (
            aws_sdk_qbusiness.types.attachments_control_mode.deserialize_json(
                data["attachmentsControlMode"]
            )
        )
    else:
        raise DeserializationError(
            "AttachmentsConfiguration.attachments_control_mode required"
        )
    return out
