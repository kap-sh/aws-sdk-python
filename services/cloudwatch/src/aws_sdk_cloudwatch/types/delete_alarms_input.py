"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DeleteAlarmsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.alarm_names


class DeleteAlarmsInput(TypedDict, closed=True):
    alarm_names: NotRequired["aws_sdk_cloudwatch.types.alarm_names.AlarmNames"]
    """<p>The alarms to be deleted. Do not enclose the alarm names in quote marks.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAlarmsInput) -> dict:
    out: dict = {}
    if "alarm_names" in value:
        import aws_sdk_cloudwatch.types.alarm_names

        out["AlarmNames"] = aws_sdk_cloudwatch.types.alarm_names.serialize_aws_json_1_0(
            value["alarm_names"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAlarmsInput:
    out: DeleteAlarmsInput = {}  # type: ignore[typeddict-item]
    if "AlarmNames" in data:
        import aws_sdk_cloudwatch.types.alarm_names

        out["alarm_names"] = (
            aws_sdk_cloudwatch.types.alarm_names.deserialize_aws_json_1_0(
                data["AlarmNames"]
            )
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteAlarmsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "alarm_names" in value:
        import aws_sdk_cloudwatch.types.alarm_names

        aws_sdk_cloudwatch.types.alarm_names.serialize_query(
            value["alarm_names"], pairs, f"{prefix}.AlarmNames"
        )


def deserialize_query(el: Element) -> DeleteAlarmsInput:
    out: DeleteAlarmsInput = {}  # type: ignore[typeddict-item]
    child_alarm_names = el.find("AlarmNames")
    if child_alarm_names is not None:
        import aws_sdk_cloudwatch.types.alarm_names

        out["alarm_names"] = aws_sdk_cloudwatch.types.alarm_names.deserialize_query(
            child_alarm_names
        )
    return out
