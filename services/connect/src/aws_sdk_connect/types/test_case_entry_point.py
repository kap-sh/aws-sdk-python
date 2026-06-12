"""Generated from Smithy shape ``com.amazonaws.connect#TestCaseEntryPoint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.chat_entry_point_parameters
    import aws_sdk_connect.types.test_case_entry_point_type
    import aws_sdk_connect.types.voice_call_entry_point_parameters


class TestCaseEntryPoint(TypedDict):
    type: NotRequired[
        "aws_sdk_connect.types.test_case_entry_point_type.TestCaseEntryPointType"
    ]
    """<p>The type of entry point.</p>"""
    voice_call_entry_point_parameters: NotRequired[
        "aws_sdk_connect.types.voice_call_entry_point_parameters.VoiceCallEntryPointParameters"
    ]
    """<p>Parameters for voice call entry point.</p>"""
    chat_entry_point_parameters: NotRequired[
        "aws_sdk_connect.types.chat_entry_point_parameters.ChatEntryPointParameters"
    ]
    """<p>Parameters for chat entry point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseEntryPoint) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_connect.types.test_case_entry_point_type

        out["Type"] = aws_sdk_connect.types.test_case_entry_point_type.serialize_json(
            value["type"]
        )
    if "voice_call_entry_point_parameters" in value:
        import aws_sdk_connect.types.voice_call_entry_point_parameters

        out["VoiceCallEntryPointParameters"] = (
            aws_sdk_connect.types.voice_call_entry_point_parameters.serialize_json(
                value["voice_call_entry_point_parameters"]
            )
        )
    if "chat_entry_point_parameters" in value:
        import aws_sdk_connect.types.chat_entry_point_parameters

        out["ChatEntryPointParameters"] = (
            aws_sdk_connect.types.chat_entry_point_parameters.serialize_json(
                value["chat_entry_point_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestCaseEntryPoint:
    out: TestCaseEntryPoint = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_connect.types.test_case_entry_point_type

        out["type"] = aws_sdk_connect.types.test_case_entry_point_type.deserialize_json(
            data["Type"]
        )
    if "VoiceCallEntryPointParameters" in data:
        import aws_sdk_connect.types.voice_call_entry_point_parameters

        out["voice_call_entry_point_parameters"] = (
            aws_sdk_connect.types.voice_call_entry_point_parameters.deserialize_json(
                data["VoiceCallEntryPointParameters"]
            )
        )
    if "ChatEntryPointParameters" in data:
        import aws_sdk_connect.types.chat_entry_point_parameters

        out["chat_entry_point_parameters"] = (
            aws_sdk_connect.types.chat_entry_point_parameters.deserialize_json(
                data["ChatEntryPointParameters"]
            )
        )
    return out
