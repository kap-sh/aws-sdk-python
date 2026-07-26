"""Generated from Smithy shape ``com.amazonaws.iotevents#InputSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events.types.input_arn
    import capo_iot_events.types.input_description
    import capo_iot_events.types.input_name
    import capo_iot_events.types.input_status
    import capo_iot_events.types.timestamp


class InputSummary(TypedDict, closed=True):
    input_name: NotRequired["capo_iot_events.types.input_name.InputName"]
    """<p>The name of the input.</p>"""
    input_description: NotRequired[
        "capo_iot_events.types.input_description.InputDescription"
    ]
    """<p>A brief description of the input.</p>"""
    input_arn: NotRequired["capo_iot_events.types.input_arn.InputArn"]
    """<p>The ARN of the input.</p>"""
    creation_time: NotRequired["capo_iot_events.types.timestamp.Timestamp"]
    """<p>The time the input was created.</p>"""
    last_update_time: NotRequired["capo_iot_events.types.timestamp.Timestamp"]
    """<p>The last time the input was updated.</p>"""
    status: NotRequired["capo_iot_events.types.input_status.InputStatus"]
    """<p>The status of the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputSummary) -> dict:
    out: dict = {}
    if "input_name" in value:
        out["inputName"] = value["input_name"]
    if "input_description" in value:
        out["inputDescription"] = value["input_description"]
    if "input_arn" in value:
        out["inputArn"] = value["input_arn"]
    if "creation_time" in value:
        import capo_iot_events.types.timestamp

        out["creationTime"] = capo_iot_events.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_update_time" in value:
        import capo_iot_events.types.timestamp

        out["lastUpdateTime"] = capo_iot_events.types.timestamp.serialize_json(
            value["last_update_time"]
        )
    if "status" in value:
        import capo_iot_events.types.input_status

        out["status"] = capo_iot_events.types.input_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> InputSummary:
    out: InputSummary = {}  # type: ignore[typeddict-item]
    if "inputName" in data:
        out["input_name"] = data["inputName"]
    if "inputDescription" in data:
        out["input_description"] = data["inputDescription"]
    if "inputArn" in data:
        out["input_arn"] = data["inputArn"]
    if "creationTime" in data:
        import capo_iot_events.types.timestamp

        out["creation_time"] = capo_iot_events.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if "lastUpdateTime" in data:
        import capo_iot_events.types.timestamp

        out["last_update_time"] = capo_iot_events.types.timestamp.deserialize_json(
            data["lastUpdateTime"]
        )
    if "status" in data:
        import capo_iot_events.types.input_status

        out["status"] = capo_iot_events.types.input_status.deserialize_json(
            data["status"]
        )
    return out
