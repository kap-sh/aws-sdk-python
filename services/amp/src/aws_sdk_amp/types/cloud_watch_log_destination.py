"""Generated from Smithy shape ``com.amazonaws.amp#CloudWatchLogDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_amp.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_amp.types.log_group_arn


class CloudWatchLogDestination(TypedDict, closed=True):
    log_group_arn: "aws_sdk_amp.types.log_group_arn.LogGroupArn"
    """<p>The ARN of the CloudWatch log group to which the vended log data will be published. This log group must exist prior to calling this operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLogDestination) -> dict:
    out: dict = {}
    out["logGroupArn"] = value["log_group_arn"]
    return out


def deserialize_json(data: dict) -> CloudWatchLogDestination:
    out: CloudWatchLogDestination = {}  # type: ignore[typeddict-item]
    if "logGroupArn" in data:
        out["log_group_arn"] = data["logGroupArn"]
    else:
        raise DeserializationError("CloudWatchLogDestination.log_group_arn required")
    return out
