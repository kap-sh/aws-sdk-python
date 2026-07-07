"""Generated from Smithy shape ``com.amazonaws.ssm#Alarm``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm.types.alarm_name


class Alarm(TypedDict, closed=True):
    name: "aws_sdk_ssm.types.alarm_name.AlarmName"
    """<p>The name of your CloudWatch alarm.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Alarm) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Alarm:
    out: Alarm = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Alarm.name required")
    return out
