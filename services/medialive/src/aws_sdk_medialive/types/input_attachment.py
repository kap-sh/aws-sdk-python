"""Generated from Smithy shape ``com.amazonaws.medialive#InputAttachment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.automatic_input_failover_settings
    import aws_sdk_medialive.types.input_settings


class InputAttachment(TypedDict, closed=True):
    automatic_input_failover_settings: NotRequired[
        "aws_sdk_medialive.types.automatic_input_failover_settings.AutomaticInputFailoverSettings"
    ]
    """User-specified settings for defining what the conditions are for declaring the input unhealthy and failing over to a different input."""
    input_attachment_name: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """User-specified name for the attachment. This is required if the user wants to use this input in an input switch action."""
    input_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ID of the input"""
    input_settings: NotRequired["aws_sdk_medialive.types.input_settings.InputSettings"]
    """Settings of an input (caption selector, etc.)"""
    logical_interface_names: NotRequired[
        "aws_sdk_medialive.types.__list_of__string.__listOf__string"
    ]
    """Optional assignment of an input to a logical interface on the Node. Only applies to on premises channels."""


# --- restJson1 ser/de ---
def serialize_json(value: InputAttachment) -> dict:
    out: dict = {}
    if "automatic_input_failover_settings" in value:
        import aws_sdk_medialive.types.automatic_input_failover_settings

        out["automaticInputFailoverSettings"] = (
            aws_sdk_medialive.types.automatic_input_failover_settings.serialize_json(
                value["automatic_input_failover_settings"]
            )
        )
    if "input_attachment_name" in value:
        out["inputAttachmentName"] = value["input_attachment_name"]
    if "input_id" in value:
        out["inputId"] = value["input_id"]
    if "input_settings" in value:
        import aws_sdk_medialive.types.input_settings

        out["inputSettings"] = aws_sdk_medialive.types.input_settings.serialize_json(
            value["input_settings"]
        )
    if "logical_interface_names" in value:
        import aws_sdk_medialive.types.__list_of__string

        out["logicalInterfaceNames"] = (
            aws_sdk_medialive.types.__list_of__string.serialize_json(
                value["logical_interface_names"]
            )
        )
    return out


def deserialize_json(data: dict) -> InputAttachment:
    out: InputAttachment = {}  # type: ignore[typeddict-item]
    if "automaticInputFailoverSettings" in data:
        import aws_sdk_medialive.types.automatic_input_failover_settings

        out["automatic_input_failover_settings"] = (
            aws_sdk_medialive.types.automatic_input_failover_settings.deserialize_json(
                data["automaticInputFailoverSettings"]
            )
        )
    if "inputAttachmentName" in data:
        out["input_attachment_name"] = data["inputAttachmentName"]
    if "inputId" in data:
        out["input_id"] = data["inputId"]
    if "inputSettings" in data:
        import aws_sdk_medialive.types.input_settings

        out["input_settings"] = aws_sdk_medialive.types.input_settings.deserialize_json(
            data["inputSettings"]
        )
    if "logicalInterfaceNames" in data:
        import aws_sdk_medialive.types.__list_of__string

        out["logical_interface_names"] = (
            aws_sdk_medialive.types.__list_of__string.deserialize_json(
                data["logicalInterfaceNames"]
            )
        )
    return out
