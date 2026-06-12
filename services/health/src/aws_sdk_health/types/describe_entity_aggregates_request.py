"""Generated from Smithy shape ``com.amazonaws.health#DescribeEntityAggregatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_health.types.event_arns_list


class DescribeEntityAggregatesRequest(TypedDict):
    event_arns: NotRequired["aws_sdk_health.types.event_arns_list.EventArnsList"]
    """<p>A list of event ARNs (unique identifiers). For example: <code>\"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456\", \"arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101\"</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEntityAggregatesRequest) -> dict:
    out: dict = {}
    if "event_arns" in value:
        import aws_sdk_health.types.event_arns_list

        out["eventArns"] = aws_sdk_health.types.event_arns_list.serialize_aws_json_1_1(
            value["event_arns"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEntityAggregatesRequest:
    out: DescribeEntityAggregatesRequest = {}  # type: ignore[typeddict-item]
    if "eventArns" in data:
        import aws_sdk_health.types.event_arns_list

        out["event_arns"] = (
            aws_sdk_health.types.event_arns_list.deserialize_aws_json_1_1(
                data["eventArns"]
            )
        )
    return out
