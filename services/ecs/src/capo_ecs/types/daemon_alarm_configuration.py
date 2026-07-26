"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonAlarmConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boolean
    import capo_ecs.types.string_list


class DaemonAlarmConfiguration(TypedDict, closed=True):
    alarm_names: NotRequired["capo_ecs.types.string_list.StringList"]
    """<p>The CloudWatch alarm names to monitor during a daemon deployment.</p>"""
    enable: "capo_ecs.types.boolean.Boolean"
    """<p>Determines whether to use the CloudWatch alarm option in the daemon deployment process. The default value is <code>false</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonAlarmConfiguration) -> dict:
    out: dict = {}
    if "alarm_names" in value:
        import capo_ecs.types.string_list

        out["alarmNames"] = capo_ecs.types.string_list.serialize_aws_json_1_1(
            value["alarm_names"]
        )
    out["enable"] = value.get("enable", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DaemonAlarmConfiguration:
    out: DaemonAlarmConfiguration = {}  # type: ignore[typeddict-item]
    if "alarmNames" in data:
        import capo_ecs.types.string_list

        out["alarm_names"] = capo_ecs.types.string_list.deserialize_aws_json_1_1(
            data["alarmNames"]
        )
    if "enable" in data:
        out["enable"] = data["enable"]
    else:
        out["enable"] = False
    return out
