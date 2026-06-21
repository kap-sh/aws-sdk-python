"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#FieldsData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudwatch_logs._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.data


class FieldsData(TypedDict):
    data: NotRequired["aws_sdk_cloudwatch_logs.types.data.Data"]
    """<p>The actual log data content returned in the streaming response. This contains the fields and values of the log event in a structured format that can be parsed and processed by the client.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FieldsData) -> dict:
    out: dict = {}
    if "data" in value:
        import aws_sdk_cloudwatch_logs.types.data

        out["data"] = aws_sdk_cloudwatch_logs.types.data.serialize_aws_json_1_1(
            value["data"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FieldsData:
    out: FieldsData = {}  # type: ignore[typeddict-item]
    if "data" in data:
        import aws_sdk_cloudwatch_logs.types.data

        out["data"] = aws_sdk_cloudwatch_logs.types.data.deserialize_aws_json_1_1(
            data["data"]
        )
    return out


def serialize_event_aws_json_1_1(value: FieldsData) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "fields"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_aws_json_1_1(message: Message) -> FieldsData:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: FieldsData = {}  # type: ignore[typeddict-item]
    return out
