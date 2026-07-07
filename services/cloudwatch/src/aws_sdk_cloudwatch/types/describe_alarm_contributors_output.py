"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DescribeAlarmContributorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.alarm_contributors
    import aws_sdk_cloudwatch.types.next_token


class DescribeAlarmContributorsOutput(TypedDict, closed=True):
    alarm_contributors: NotRequired[
        "aws_sdk_cloudwatch.types.alarm_contributors.AlarmContributors"
    ]
    """<p>A list of alarm contributors that provide details about the individual time series contributing to the alarm's state.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch.types.next_token.NextToken"]
    """<p>The token that marks the start of the next batch of returned results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAlarmContributorsOutput) -> dict:
    out: dict = {}
    if "alarm_contributors" in value:
        import aws_sdk_cloudwatch.types.alarm_contributors

        out["AlarmContributors"] = (
            aws_sdk_cloudwatch.types.alarm_contributors.serialize_aws_json_1_0(
                value["alarm_contributors"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAlarmContributorsOutput:
    out: DescribeAlarmContributorsOutput = {}  # type: ignore[typeddict-item]
    if "AlarmContributors" in data:
        import aws_sdk_cloudwatch.types.alarm_contributors

        out["alarm_contributors"] = (
            aws_sdk_cloudwatch.types.alarm_contributors.deserialize_aws_json_1_0(
                data["AlarmContributors"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAlarmContributorsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "alarm_contributors" in value:
        import aws_sdk_cloudwatch.types.alarm_contributors

        aws_sdk_cloudwatch.types.alarm_contributors.serialize_query(
            value["alarm_contributors"], pairs, f"{prefix}.AlarmContributors"
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeAlarmContributorsOutput:
    out: DescribeAlarmContributorsOutput = {}  # type: ignore[typeddict-item]
    child_alarm_contributors = el.find("AlarmContributors")
    if child_alarm_contributors is not None:
        import aws_sdk_cloudwatch.types.alarm_contributors

        out["alarm_contributors"] = (
            aws_sdk_cloudwatch.types.alarm_contributors.deserialize_query(
                child_alarm_contributors
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
