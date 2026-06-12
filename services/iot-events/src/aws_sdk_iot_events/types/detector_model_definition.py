"""Generated from Smithy shape ``com.amazonaws.iotevents#DetectorModelDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.state_name
    import aws_sdk_iot_events.types.states


class DetectorModelDefinition(TypedDict):
    states: "aws_sdk_iot_events.types.states.States"
    """<p>Information about the states of the detector.</p>"""
    initial_state_name: "aws_sdk_iot_events.types.state_name.StateName"
    """<p>The state that is entered at the creation of each detector (instance).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectorModelDefinition) -> dict:
    out: dict = {}
    import aws_sdk_iot_events.types.states

    out["states"] = aws_sdk_iot_events.types.states.serialize_json(value["states"])
    out["initialStateName"] = value["initial_state_name"]
    return out


def deserialize_json(data: dict) -> DetectorModelDefinition:
    out: DetectorModelDefinition = {}  # type: ignore[typeddict-item]
    if "states" in data:
        import aws_sdk_iot_events.types.states

        out["states"] = aws_sdk_iot_events.types.states.deserialize_json(data["states"])
    else:
        raise DeserializationError("DetectorModelDefinition.states required")
    if "initialStateName" in data:
        out["initial_state_name"] = data["initialStateName"]
    else:
        raise DeserializationError(
            "DetectorModelDefinition.initial_state_name required"
        )
    return out
