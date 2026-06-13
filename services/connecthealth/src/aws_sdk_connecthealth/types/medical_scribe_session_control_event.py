"""Generated from Smithy shape ``com.amazonaws.connecthealth#MedicalScribeSessionControlEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connecthealth.types.medical_scribe_session_control_event_type


class MedicalScribeSessionControlEvent(TypedDict):
    type: NotRequired[
        "aws_sdk_connecthealth.types.medical_scribe_session_control_event_type.MedicalScribeSessionControlEventType"
    ]
    """<p>The type of session control event</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeSessionControlEvent) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_connecthealth.types.medical_scribe_session_control_event_type

        out["type"] = (
            aws_sdk_connecthealth.types.medical_scribe_session_control_event_type.serialize_json(
                value["type"]
            )
        )
    return out


def deserialize_json(data: dict) -> MedicalScribeSessionControlEvent:
    out: MedicalScribeSessionControlEvent = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_connecthealth.types.medical_scribe_session_control_event_type

        out["type"] = (
            aws_sdk_connecthealth.types.medical_scribe_session_control_event_type.deserialize_json(
                data["type"]
            )
        )
    return out
