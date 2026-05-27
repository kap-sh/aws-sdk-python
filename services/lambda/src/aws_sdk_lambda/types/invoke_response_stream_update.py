"""Generated from Smithy shape ``com.amazonaws.lambda#InvokeResponseStreamUpdate``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.blob


class InvokeResponseStreamUpdate(TypedDict):
    payload: NotRequired["aws_sdk_lambda.types.blob.Blob"]
    """<p>Data returned by your Lambda function.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeResponseStreamUpdate) -> dict:
    out: dict = {}
    if "payload" in value:
        import aws_sdk_lambda.types.blob

        out["Payload"] = aws_sdk_lambda.types.blob.serialize_json(value["payload"])
    return out


def deserialize_json(data: dict) -> InvokeResponseStreamUpdate:
    out: InvokeResponseStreamUpdate = {}  # type: ignore[typeddict-item]
    if "Payload" in data:
        import aws_sdk_lambda.types.blob

        out["payload"] = aws_sdk_lambda.types.blob.deserialize_json(data["Payload"])
    return out
