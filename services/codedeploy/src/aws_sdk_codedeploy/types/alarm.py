"""Generated from Smithy shape ``com.amazonaws.codedeploy#Alarm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codedeploy.types.alarm_name


class Alarm(TypedDict, closed=True):
    name: NotRequired["aws_sdk_codedeploy.types.alarm_name.AlarmName"]
    """<p>The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only once in a list of alarms.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Alarm) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Alarm:
    out: Alarm = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    return out
