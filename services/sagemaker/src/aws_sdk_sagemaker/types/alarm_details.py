"""Generated from Smithy shape ``com.amazonaws.sagemaker#AlarmDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.alarm_name


class AlarmDetails(TypedDict):
    alarm_name: NotRequired["aws_sdk_sagemaker.types.alarm_name.AlarmName"]
    """<p>The name of the alarm.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlarmDetails) -> dict:
    out: dict = {}
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AlarmDetails:
    out: AlarmDetails = {}  # type: ignore[typeddict-item]
    if "AlarmName" in data:
        out["alarm_name"] = data["AlarmName"]
    return out
