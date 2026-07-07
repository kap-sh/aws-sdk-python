"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#DetectorSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.detector_model_name
    import aws_sdk_iot_events_data.types.detector_model_version
    import aws_sdk_iot_events_data.types.detector_state_summary
    import aws_sdk_iot_events_data.types.key_value
    import aws_sdk_iot_events_data.types.timestamp


class DetectorSummary(TypedDict, closed=True):
    detector_model_name: NotRequired[
        "aws_sdk_iot_events_data.types.detector_model_name.DetectorModelName"
    ]
    """<p>The name of the detector model that created this detector (instance).</p>"""
    key_value: NotRequired["aws_sdk_iot_events_data.types.key_value.KeyValue"]
    """<p>The value of the key (identifying the device or system) that caused the creation of this detector (instance).</p>"""
    detector_model_version: NotRequired[
        "aws_sdk_iot_events_data.types.detector_model_version.DetectorModelVersion"
    ]
    """<p>The version of the detector model that created this detector (instance).</p>"""
    state: NotRequired[
        "aws_sdk_iot_events_data.types.detector_state_summary.DetectorStateSummary"
    ]
    """<p>The current state of the detector (instance).</p>"""
    creation_time: NotRequired["aws_sdk_iot_events_data.types.timestamp.Timestamp"]
    """<p>The time the detector (instance) was created.</p>"""
    last_update_time: NotRequired["aws_sdk_iot_events_data.types.timestamp.Timestamp"]
    """<p>The time the detector (instance) was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectorSummary) -> dict:
    out: dict = {}
    if "detector_model_name" in value:
        out["detectorModelName"] = value["detector_model_name"]
    if "key_value" in value:
        out["keyValue"] = value["key_value"]
    if "detector_model_version" in value:
        out["detectorModelVersion"] = value["detector_model_version"]
    if "state" in value:
        import aws_sdk_iot_events_data.types.detector_state_summary

        out["state"] = (
            aws_sdk_iot_events_data.types.detector_state_summary.serialize_json(
                value["state"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_iot_events_data.types.timestamp

        out["creationTime"] = aws_sdk_iot_events_data.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_update_time" in value:
        import aws_sdk_iot_events_data.types.timestamp

        out["lastUpdateTime"] = aws_sdk_iot_events_data.types.timestamp.serialize_json(
            value["last_update_time"]
        )
    return out


def deserialize_json(data: dict) -> DetectorSummary:
    out: DetectorSummary = {}  # type: ignore[typeddict-item]
    if "detectorModelName" in data:
        out["detector_model_name"] = data["detectorModelName"]
    if "keyValue" in data:
        out["key_value"] = data["keyValue"]
    if "detectorModelVersion" in data:
        out["detector_model_version"] = data["detectorModelVersion"]
    if "state" in data:
        import aws_sdk_iot_events_data.types.detector_state_summary

        out["state"] = (
            aws_sdk_iot_events_data.types.detector_state_summary.deserialize_json(
                data["state"]
            )
        )
    if "creationTime" in data:
        import aws_sdk_iot_events_data.types.timestamp

        out["creation_time"] = aws_sdk_iot_events_data.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if "lastUpdateTime" in data:
        import aws_sdk_iot_events_data.types.timestamp

        out["last_update_time"] = (
            aws_sdk_iot_events_data.types.timestamp.deserialize_json(
                data["lastUpdateTime"]
            )
        )
    return out
