"""Generated from Smithy shape ``com.amazonaws.emr#ScalingTrigger``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.cloud_watch_alarm_definition


class ScalingTrigger(TypedDict, closed=True):
    cloud_watch_alarm_definition: NotRequired[
        "capo_emr.types.cloud_watch_alarm_definition.CloudWatchAlarmDefinition"
    ]
    """<p>The definition of a CloudWatch metric alarm. When the defined alarm conditions are met along with other trigger parameters, scaling activity begins.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScalingTrigger) -> dict:
    out: dict = {}
    if "cloud_watch_alarm_definition" in value:
        import capo_emr.types.cloud_watch_alarm_definition

        out["CloudWatchAlarmDefinition"] = (
            capo_emr.types.cloud_watch_alarm_definition.serialize_aws_json_1_1(
                value["cloud_watch_alarm_definition"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ScalingTrigger:
    out: ScalingTrigger = {}  # type: ignore[typeddict-item]
    if "CloudWatchAlarmDefinition" in data:
        import capo_emr.types.cloud_watch_alarm_definition

        out["cloud_watch_alarm_definition"] = (
            capo_emr.types.cloud_watch_alarm_definition.deserialize_aws_json_1_1(
                data["CloudWatchAlarmDefinition"]
            )
        )
    return out
