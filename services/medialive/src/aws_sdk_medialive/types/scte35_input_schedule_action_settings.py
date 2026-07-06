"""Generated from Smithy shape ``com.amazonaws.medialive#Scte35InputScheduleActionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.scte35_input_mode


class Scte35InputScheduleActionSettings(TypedDict, closed=True):
    input_attachment_name_reference: NotRequired[
        "aws_sdk_medialive.types.__string.__string"
    ]
    r"""In fixed mode, enter the name of the input attachment that you want to use as a SCTE-35 input. (Don't enter the ID of the input.)\""""
    mode: NotRequired["aws_sdk_medialive.types.scte35_input_mode.Scte35InputMode"]
    """Whether the SCTE-35 input should be the active input or a fixed input."""


# --- restJson1 ser/de ---
def serialize_json(value: Scte35InputScheduleActionSettings) -> dict:
    out: dict = {}
    if "input_attachment_name_reference" in value:
        out["inputAttachmentNameReference"] = value["input_attachment_name_reference"]
    if "mode" in value:
        import aws_sdk_medialive.types.scte35_input_mode

        out["mode"] = aws_sdk_medialive.types.scte35_input_mode.serialize_json(
            value["mode"]
        )
    return out


def deserialize_json(data: dict) -> Scte35InputScheduleActionSettings:
    out: Scte35InputScheduleActionSettings = {}  # type: ignore[typeddict-item]
    if "inputAttachmentNameReference" in data:
        out["input_attachment_name_reference"] = data["inputAttachmentNameReference"]
    if "mode" in data:
        import aws_sdk_medialive.types.scte35_input_mode

        out["mode"] = aws_sdk_medialive.types.scte35_input_mode.deserialize_json(
            data["mode"]
        )
    return out
