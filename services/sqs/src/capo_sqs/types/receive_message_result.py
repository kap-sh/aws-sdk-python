"""Generated from Smithy shape ``com.amazonaws.sqs#ReceiveMessageResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sqs.types.message_list


class ReceiveMessageResult(TypedDict, closed=True):
    messages: NotRequired["capo_sqs.types.message_list.MessageList"]
    """<p>A list of messages.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ReceiveMessageResult) -> dict:
    out: dict = {}
    if "messages" in value:
        import capo_sqs.types.message_list

        out["Messages"] = capo_sqs.types.message_list.serialize_aws_json_1_0(
            value["messages"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ReceiveMessageResult:
    out: ReceiveMessageResult = {}  # type: ignore[typeddict-item]
    if data.get("Messages") is not None:
        import capo_sqs.types.message_list

        out["messages"] = capo_sqs.types.message_list.deserialize_aws_json_1_0(
            data["Messages"]
        )
    return out
