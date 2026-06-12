"""Generated from Smithy shape ``com.amazonaws.sqs#ReceiveMessageResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sqs.types.message_list


class ReceiveMessageResult(TypedDict):
    messages: NotRequired["aws_sdk_sqs.types.message_list.MessageList"]
    """<p>A list of messages.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReceiveMessageResult) -> dict:
    out: dict = {}
    if "messages" in value:
        import aws_sdk_sqs.types.message_list

        out["Messages"] = aws_sdk_sqs.types.message_list.serialize_aws_json_1_0(
            value["messages"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReceiveMessageResult:
    out: ReceiveMessageResult = {}  # type: ignore[typeddict-item]
    if "Messages" in data:
        import aws_sdk_sqs.types.message_list

        out["messages"] = aws_sdk_sqs.types.message_list.deserialize_aws_json_1_0(
            data["Messages"]
        )
    return out
