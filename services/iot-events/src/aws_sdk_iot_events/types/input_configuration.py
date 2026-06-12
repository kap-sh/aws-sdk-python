"""Generated from Smithy shape ``com.amazonaws.iotevents#InputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot_events.types.input_arn
    import aws_sdk_iot_events.types.input_description
    import aws_sdk_iot_events.types.input_name
    import aws_sdk_iot_events.types.input_status
    import aws_sdk_iot_events.types.timestamp


class InputConfiguration(TypedDict):
    input_name: "aws_sdk_iot_events.types.input_name.InputName"
    """<p>The name of the input.</p>"""
    input_description: NotRequired[
        "aws_sdk_iot_events.types.input_description.InputDescription"
    ]
    """<p>A brief description of the input.</p>"""
    input_arn: "aws_sdk_iot_events.types.input_arn.InputArn"
    """<p>The ARN of the input.</p>"""
    creation_time: "aws_sdk_iot_events.types.timestamp.Timestamp"
    """<p>The time the input was created.</p>"""
    last_update_time: "aws_sdk_iot_events.types.timestamp.Timestamp"
    """<p>The last time the input was updated.</p>"""
    status: "aws_sdk_iot_events.types.input_status.InputStatus"
    """<p>The status of the input.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputConfiguration) -> dict:
    out: dict = {}
    out["inputName"] = value["input_name"]
    if "input_description" in value:
        out["inputDescription"] = value["input_description"]
    out["inputArn"] = value["input_arn"]
    import aws_sdk_iot_events.types.timestamp

    out["creationTime"] = aws_sdk_iot_events.types.timestamp.serialize_json(
        value["creation_time"]
    )
    import aws_sdk_iot_events.types.timestamp

    out["lastUpdateTime"] = aws_sdk_iot_events.types.timestamp.serialize_json(
        value["last_update_time"]
    )
    import aws_sdk_iot_events.types.input_status

    out["status"] = aws_sdk_iot_events.types.input_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> InputConfiguration:
    out: InputConfiguration = {}  # type: ignore[typeddict-item]
    if "inputName" in data:
        out["input_name"] = data["inputName"]
    else:
        raise DeserializationError("InputConfiguration.input_name required")
    if "inputDescription" in data:
        out["input_description"] = data["inputDescription"]
    if "inputArn" in data:
        out["input_arn"] = data["inputArn"]
    else:
        raise DeserializationError("InputConfiguration.input_arn required")
    if "creationTime" in data:
        import aws_sdk_iot_events.types.timestamp

        out["creation_time"] = aws_sdk_iot_events.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("InputConfiguration.creation_time required")
    if "lastUpdateTime" in data:
        import aws_sdk_iot_events.types.timestamp

        out["last_update_time"] = aws_sdk_iot_events.types.timestamp.deserialize_json(
            data["lastUpdateTime"]
        )
    else:
        raise DeserializationError("InputConfiguration.last_update_time required")
    if "status" in data:
        import aws_sdk_iot_events.types.input_status

        out["status"] = aws_sdk_iot_events.types.input_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("InputConfiguration.status required")
    return out
