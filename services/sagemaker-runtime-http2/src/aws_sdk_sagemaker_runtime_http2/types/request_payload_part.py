"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#RequestPayloadPart``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker_runtime_http2._protocol.eventstream import HeaderValue, Message

if TYPE_CHECKING:
    import aws_sdk_sagemaker_runtime_http2.types.sensitive_blob


class RequestPayloadPart(TypedDict):
    bytes: NotRequired[
        "aws_sdk_sagemaker_runtime_http2.types.sensitive_blob.SensitiveBlob"
    ]
    """<p>The payload bytes.</p>"""
    data_type: NotRequired["str"]
    r"""<p>Data type header. Can be one of these possible values: \"UTF8\", \"BINARY\".</p>"""
    completion_state: NotRequired["str"]
    r"""<p>Completion state header. Can be one of these possible values: \"PARTIAL\", \"COMPLETE\".</p>"""
    p: NotRequired["str"]
    """<p>Padding string for alignment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RequestPayloadPart) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RequestPayloadPart:
    out: RequestPayloadPart = {}  # type: ignore[typeddict-item]
    return out


def serialize_event_json(value: RequestPayloadPart) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "PayloadPart"}
    payload = b""
    if "data_type" in value:
        headers["DataType"] = value["data_type"]
    if "completion_state" in value:
        headers["CompletionState"] = value["completion_state"]
    if "p" in value:
        headers["P"] = value["p"]
    payload = value["bytes"]
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> RequestPayloadPart:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: RequestPayloadPart = {}  # type: ignore[typeddict-item]
    if "DataType" in headers:
        out["data_type"] = headers["DataType"]
    if "CompletionState" in headers:
        out["completion_state"] = headers["CompletionState"]
    if "P" in headers:
        out["p"] = headers["P"]
    if payload:
        out["bytes"] = payload
    return out
