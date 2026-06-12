"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#DeleteDetectorRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.delete_detector_request

DeleteDetectorRequests: TypeAlias = list[
    "aws_sdk_iot_events_data.types.delete_detector_request.DeleteDetectorRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDetectorRequests) -> list:
    import aws_sdk_iot_events_data.types.delete_detector_request

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_events_data.types.delete_detector_request.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DeleteDetectorRequests:
    import aws_sdk_iot_events_data.types.delete_detector_request

    out: DeleteDetectorRequests = []
    for item in data:
        out.append(
            aws_sdk_iot_events_data.types.delete_detector_request.deserialize_json(item)
        )
    return out
