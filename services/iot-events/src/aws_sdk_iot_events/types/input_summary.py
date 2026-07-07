"""Generated from Smithy shape ``com.amazonaws.iotevents#InputSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.input_arn
    import aws_sdk_iot_events.types.input_description
    import aws_sdk_iot_events.types.input_name
    import aws_sdk_iot_events.types.input_status
    import aws_sdk_iot_events.types.timestamp


class InputSummary(TypedDict, closed=True):
    input_name: NotRequired["aws_sdk_iot_events.types.input_name.InputName"]
    """<p>The name of the input.</p>"""
    input_description: NotRequired[
        "aws_sdk_iot_events.types.input_description.InputDescription"
    ]
    """<p>A brief description of the input.</p>"""
    input_arn: NotRequired["aws_sdk_iot_events.types.input_arn.InputArn"]
    """<p>The ARN of the input.</p>"""
    creation_time: NotRequired["aws_sdk_iot_events.types.timestamp.Timestamp"]
    """<p>The time the input was created.</p>"""
    last_update_time: NotRequired["aws_sdk_iot_events.types.timestamp.Timestamp"]
    """<p>The last time the input was updated.</p>"""
    status: NotRequired["aws_sdk_iot_events.types.input_status.InputStatus"]
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
        import aws_sdk_iot_events.types.timestamp

        out["creationTime"] = aws_sdk_iot_events.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_update_time" in value:
        import aws_sdk_iot_events.types.timestamp

        out["lastUpdateTime"] = aws_sdk_iot_events.types.timestamp.serialize_json(
            value["last_update_time"]
        )
    if "status" in value:
        import aws_sdk_iot_events.types.input_status

        out["status"] = aws_sdk_iot_events.types.input_status.serialize_json(
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
        import aws_sdk_iot_events.types.timestamp

        out["creation_time"] = aws_sdk_iot_events.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if "lastUpdateTime" in data:
        import aws_sdk_iot_events.types.timestamp

        out["last_update_time"] = aws_sdk_iot_events.types.timestamp.deserialize_json(
            data["lastUpdateTime"]
        )
    if "status" in data:
        import aws_sdk_iot_events.types.input_status

        out["status"] = aws_sdk_iot_events.types.input_status.deserialize_json(
            data["status"]
        )
    return out
