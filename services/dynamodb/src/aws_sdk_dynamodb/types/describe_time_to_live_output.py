"""Generated from Smithy shape ``com.amazonaws.dynamodb#DescribeTimeToLiveOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.time_to_live_description


class DescribeTimeToLiveOutput(TypedDict):
    time_to_live_description: NotRequired[
        "aws_sdk_dynamodb.types.time_to_live_description.TimeToLiveDescription"
    ]
    """<p></p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeTimeToLiveOutput) -> dict:
    out: dict = {}
    if "time_to_live_description" in value:
        import aws_sdk_dynamodb.types.time_to_live_description

        out["TimeToLiveDescription"] = (
            aws_sdk_dynamodb.types.time_to_live_description.serialize_aws_json_1_0(
                value["time_to_live_description"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeTimeToLiveOutput:
    out: DescribeTimeToLiveOutput = {}  # type: ignore[typeddict-item]
    if "TimeToLiveDescription" in data:
        import aws_sdk_dynamodb.types.time_to_live_description

        out["time_to_live_description"] = (
            aws_sdk_dynamodb.types.time_to_live_description.deserialize_aws_json_1_0(
                data["TimeToLiveDescription"]
            )
        )
    return out
