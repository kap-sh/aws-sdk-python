"""Generated from Smithy shape ``com.amazonaws.sagemakerruntimehttp2#RequestPayloadPart``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

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
    if "bytes" in value:
        import aws_sdk_sagemaker_runtime_http2.types.sensitive_blob

        out["Bytes"] = (
            aws_sdk_sagemaker_runtime_http2.types.sensitive_blob.serialize_json(
                value["bytes"]
            )
        )
    if "data_type" in value:
        out["DataType"] = value["data_type"]
    if "completion_state" in value:
        out["CompletionState"] = value["completion_state"]
    if "p" in value:
        out["P"] = value["p"]
    return out


def deserialize_json(data: dict) -> RequestPayloadPart:
    out: RequestPayloadPart = {}  # type: ignore[typeddict-item]
    if "Bytes" in data:
        import aws_sdk_sagemaker_runtime_http2.types.sensitive_blob

        out["bytes"] = (
            aws_sdk_sagemaker_runtime_http2.types.sensitive_blob.deserialize_json(
                data["Bytes"]
            )
        )
    if "DataType" in data:
        out["data_type"] = data["DataType"]
    if "CompletionState" in data:
        out["completion_state"] = data["CompletionState"]
    if "P" in data:
        out["p"] = data["P"]
    return out
