"""Generated from Smithy shape ``com.amazonaws.autoscaling#Alarm``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.resource_name
    import aws_sdk_auto_scaling.types.xml_string_max_len255


class Alarm(TypedDict):
    alarm_name: NotRequired[
        "aws_sdk_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The name of the alarm.</p>"""
    alarm_arn: NotRequired["aws_sdk_auto_scaling.types.resource_name.ResourceName"]
    """<p>The Amazon Resource Name (ARN) of the alarm.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Alarm, pairs: list[tuple[str, str]], prefix: str) -> None:
    if "alarm_name" in value:
        pairs.append((f"{prefix}.AlarmName", str(value["alarm_name"])))
    if "alarm_arn" in value:
        pairs.append((f"{prefix}.AlarmARN", str(value["alarm_arn"])))


def deserialize_query(el: Element) -> Alarm:
    out: Alarm = {}  # type: ignore[typeddict-item]
    child_alarm_name = el.find("AlarmName")
    if child_alarm_name is not None:
        out["alarm_name"] = str(child_alarm_name.text or "")
    child_alarm_arn = el.find("AlarmARN")
    if child_alarm_arn is not None:
        out["alarm_arn"] = str(child_alarm_arn.text or "")
    return out
