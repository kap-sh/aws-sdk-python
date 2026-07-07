"""Generated from Smithy shape ``com.amazonaws.ssm#AlarmStateInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.alarm_name
    import aws_sdk_ssm.types.external_alarm_state


class AlarmStateInformation(TypedDict, closed=True):
    name: "aws_sdk_ssm.types.alarm_name.AlarmName"
    """<p>The name of your CloudWatch alarm.</p>"""
    state: "aws_sdk_ssm.types.external_alarm_state.ExternalAlarmState"
    """<p>The state of your CloudWatch alarm.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlarmStateInformation) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_ssm.types.external_alarm_state

    out["State"] = aws_sdk_ssm.types.external_alarm_state.serialize_aws_json_1_1(
        value["state"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AlarmStateInformation:
    out: AlarmStateInformation = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("AlarmStateInformation.name required")
    if "State" in data:
        import aws_sdk_ssm.types.external_alarm_state

        out["state"] = aws_sdk_ssm.types.external_alarm_state.deserialize_aws_json_1_1(
            data["State"]
        )
    else:
        raise DeserializationError("AlarmStateInformation.state required")
    return out
