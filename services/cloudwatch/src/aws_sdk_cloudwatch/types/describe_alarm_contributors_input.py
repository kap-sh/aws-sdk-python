"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DescribeAlarmContributorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.alarm_name
    import aws_sdk_cloudwatch.types.next_token


class DescribeAlarmContributorsInput(TypedDict, closed=True):
    alarm_name: NotRequired["aws_sdk_cloudwatch.types.alarm_name.AlarmName"]
    """<p>The name of the alarm for which to retrieve contributor information.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch.types.next_token.NextToken"]
    """<p>The token returned by a previous call to indicate that there is more data available.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAlarmContributorsInput) -> dict:
    out: dict = {}
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAlarmContributorsInput:
    out: DescribeAlarmContributorsInput = {}  # type: ignore[typeddict-item]
    if "AlarmName" in data:
        out["alarm_name"] = data["AlarmName"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAlarmContributorsInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "alarm_name" in value:
        pairs.append((f"{prefix}.AlarmName", str(value["alarm_name"])))
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeAlarmContributorsInput:
    out: DescribeAlarmContributorsInput = {}  # type: ignore[typeddict-item]
    child_alarm_name = el.find("AlarmName")
    if child_alarm_name is not None:
        out["alarm_name"] = str(child_alarm_name.text or "")
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
