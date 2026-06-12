"""Generated from Smithy shape ``com.amazonaws.sagemaker#Alarm``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.alarm_name


class Alarm(TypedDict):
    alarm_name: NotRequired["aws_sdk_sagemaker.types.alarm_name.AlarmName"]
    """<p>The name of a CloudWatch alarm in your account.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Alarm) -> dict:
    out: dict = {}
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Alarm:
    out: Alarm = {}  # type: ignore[typeddict-item]
    if "AlarmName" in data:
        out["alarm_name"] = data["AlarmName"]
    return out
