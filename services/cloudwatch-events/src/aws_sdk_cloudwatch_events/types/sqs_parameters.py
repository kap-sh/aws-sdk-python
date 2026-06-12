"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#SqsParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.message_group_id


class SqsParameters(TypedDict):
    message_group_id: NotRequired[
        "aws_sdk_cloudwatch_events.types.message_group_id.MessageGroupId"
    ]
    """<p>The FIFO message group ID to use as the target.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SqsParameters) -> dict:
    out: dict = {}
    if "message_group_id" in value:
        out["MessageGroupId"] = value["message_group_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SqsParameters:
    out: SqsParameters = {}  # type: ignore[typeddict-item]
    if "MessageGroupId" in data:
        out["message_group_id"] = data["MessageGroupId"]
    return out
