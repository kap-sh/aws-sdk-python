"""Generated from Smithy shape ``com.amazonaws.connect#TestCaseEntryPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.chat_entry_point_parameters
    import capo_connect.types.test_case_entry_point_type
    import capo_connect.types.voice_call_entry_point_parameters


class TestCaseEntryPoint(TypedDict, closed=True):
    type: NotRequired[
        "capo_connect.types.test_case_entry_point_type.TestCaseEntryPointType"
    ]
    """<p>The type of entry point.</p>"""
    voice_call_entry_point_parameters: NotRequired[
        "capo_connect.types.voice_call_entry_point_parameters.VoiceCallEntryPointParameters"
    ]
    """<p>Parameters for voice call entry point.</p>"""
    chat_entry_point_parameters: NotRequired[
        "capo_connect.types.chat_entry_point_parameters.ChatEntryPointParameters"
    ]
    """<p>Parameters for chat entry point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestCaseEntryPoint) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_connect.types.test_case_entry_point_type

        out["Type"] = capo_connect.types.test_case_entry_point_type.serialize_json(
            value["type"]
        )
    if "voice_call_entry_point_parameters" in value:
        import capo_connect.types.voice_call_entry_point_parameters

        out["VoiceCallEntryPointParameters"] = (
            capo_connect.types.voice_call_entry_point_parameters.serialize_json(
                value["voice_call_entry_point_parameters"]
            )
        )
    if "chat_entry_point_parameters" in value:
        import capo_connect.types.chat_entry_point_parameters

        out["ChatEntryPointParameters"] = (
            capo_connect.types.chat_entry_point_parameters.serialize_json(
                value["chat_entry_point_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestCaseEntryPoint:
    out: TestCaseEntryPoint = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_connect.types.test_case_entry_point_type

        out["type"] = capo_connect.types.test_case_entry_point_type.deserialize_json(
            data["Type"]
        )
    if "VoiceCallEntryPointParameters" in data:
        import capo_connect.types.voice_call_entry_point_parameters

        out["voice_call_entry_point_parameters"] = (
            capo_connect.types.voice_call_entry_point_parameters.deserialize_json(
                data["VoiceCallEntryPointParameters"]
            )
        )
    if "ChatEntryPointParameters" in data:
        import capo_connect.types.chat_entry_point_parameters

        out["chat_entry_point_parameters"] = (
            capo_connect.types.chat_entry_point_parameters.deserialize_json(
                data["ChatEntryPointParameters"]
            )
        )
    return out
