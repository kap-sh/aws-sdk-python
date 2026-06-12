"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteAlarmRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_name


class DeleteAlarmRequest(TypedDict):
    alarm_name: "aws_sdk_lightsail.types.resource_name.ResourceName"
    """<p>The name of the alarm to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAlarmRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAlarmRequest:
    out: DeleteAlarmRequest = {}  # type: ignore[typeddict-item]
    return out
