"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonAlarmConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boolean
    import aws_sdk_ecs.types.string_list


class DaemonAlarmConfiguration(TypedDict):
    alarm_names: NotRequired["aws_sdk_ecs.types.string_list.StringList"]
    """<p>The CloudWatch alarm names to monitor during a daemon deployment.</p>"""
    enable: "aws_sdk_ecs.types.boolean.Boolean"
    """<p>Determines whether to use the CloudWatch alarm option in the daemon deployment process. The default value is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonAlarmConfiguration) -> dict:
    out: dict = {}
    if "alarm_names" in value:
        import aws_sdk_ecs.types.string_list

        out["alarmNames"] = aws_sdk_ecs.types.string_list.serialize_aws_json_1_1(
            value["alarm_names"]
        )
    out["enable"] = value.get("enable", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonAlarmConfiguration:
    out: DaemonAlarmConfiguration = {}  # type: ignore[typeddict-item]
    if "alarmNames" in data:
        import aws_sdk_ecs.types.string_list

        out["alarm_names"] = aws_sdk_ecs.types.string_list.deserialize_aws_json_1_1(
            data["alarmNames"]
        )
    if "enable" in data:
        out["enable"] = data["enable"]
    else:
        out["enable"] = False
    return out
