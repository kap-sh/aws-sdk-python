"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#UpdateDetectorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.detector_model_name
    import aws_sdk_iot_events_data.types.detector_state_definition
    import aws_sdk_iot_events_data.types.key_value
    import aws_sdk_iot_events_data.types.message_id


class UpdateDetectorRequest(TypedDict):
    message_id: "aws_sdk_iot_events_data.types.message_id.MessageId"
    """<p>The ID to assign to the detector update <code>\"message\"</code>. Each <code>\"messageId\"</code> must be unique within each batch sent.</p>"""
    detector_model_name: (
        "aws_sdk_iot_events_data.types.detector_model_name.DetectorModelName"
    )
    """<p>The name of the detector model that created the detectors (instances).</p>"""
    key_value: NotRequired["aws_sdk_iot_events_data.types.key_value.KeyValue"]
    """<p>The value of the input key attribute (identifying the device or system) that caused the creation of this detector (instance).</p>"""
    state: "aws_sdk_iot_events_data.types.detector_state_definition.DetectorStateDefinition"
    """<p>The new state, variable values, and timer settings of the detector (instance).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDetectorRequest) -> dict:
    out: dict = {}
    out["messageId"] = value["message_id"]
    out["detectorModelName"] = value["detector_model_name"]
    if "key_value" in value:
        out["keyValue"] = value["key_value"]
    import aws_sdk_iot_events_data.types.detector_state_definition

    out["state"] = (
        aws_sdk_iot_events_data.types.detector_state_definition.serialize_json(
            value["state"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateDetectorRequest:
    out: UpdateDetectorRequest = {}  # type: ignore[typeddict-item]
    if "messageId" in data:
        out["message_id"] = data["messageId"]
    else:
        raise DeserializationError("UpdateDetectorRequest.message_id required")
    if "detectorModelName" in data:
        out["detector_model_name"] = data["detectorModelName"]
    else:
        raise DeserializationError("UpdateDetectorRequest.detector_model_name required")
    if "keyValue" in data:
        out["key_value"] = data["keyValue"]
    if "state" in data:
        import aws_sdk_iot_events_data.types.detector_state_definition

        out["state"] = (
            aws_sdk_iot_events_data.types.detector_state_definition.deserialize_json(
                data["state"]
            )
        )
    else:
        raise DeserializationError("UpdateDetectorRequest.state required")
    return out
