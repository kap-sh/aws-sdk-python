"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#DeleteDetectorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot_events_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.detector_model_name
    import aws_sdk_iot_events_data.types.key_value
    import aws_sdk_iot_events_data.types.message_id


class DeleteDetectorRequest(TypedDict, closed=True):
    message_id: "aws_sdk_iot_events_data.types.message_id.MessageId"
    r"""<p>The ID to assign to the <code>DeleteDetectorRequest</code>. Each <code>\"messageId\"</code> must be unique within each batch sent.</p>"""
    detector_model_name: (
        "aws_sdk_iot_events_data.types.detector_model_name.DetectorModelName"
    )
    """<p>The name of the detector model that was used to create the detector instance.</p>"""
    key_value: NotRequired["aws_sdk_iot_events_data.types.key_value.KeyValue"]
    r"""<p>The value of the <a href=\"https://docs.aws.amazon.com/iotevents/latest/apireference/API_CreateDetectorModel.html#iotevents-CreateDetectorModel-request-key\">key</a> used to identify the detector. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDetectorRequest) -> dict:
    out: dict = {}
    out["messageId"] = value["message_id"]
    out["detectorModelName"] = value["detector_model_name"]
    if "key_value" in value:
        out["keyValue"] = value["key_value"]
    return out


def deserialize_json(data: dict) -> DeleteDetectorRequest:
    out: DeleteDetectorRequest = {}  # type: ignore[typeddict-item]
    if "messageId" in data:
        out["message_id"] = data["messageId"]
    else:
        raise DeserializationError("DeleteDetectorRequest.message_id required")
    if "detectorModelName" in data:
        out["detector_model_name"] = data["detectorModelName"]
    else:
        raise DeserializationError("DeleteDetectorRequest.detector_model_name required")
    if "keyValue" in data:
        out["key_value"] = data["keyValue"]
    return out
