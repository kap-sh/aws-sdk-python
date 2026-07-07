"""Generated from Smithy shape ``com.amazonaws.ivs#BatchError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs.types.error_code
    import aws_sdk_ivs.types.error_message
    import aws_sdk_ivs.types.resource_arn


class BatchError(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_ivs.types.resource_arn.ResourceArn"]
    """<p>ARN of an IVS resource; e.g., channel.</p>"""
    code: NotRequired["aws_sdk_ivs.types.error_code.errorCode"]
    """<p>Error code.</p>"""
    message: NotRequired["aws_sdk_ivs.types.error_message.errorMessage"]
    """<p>Error message, determined by the application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchError) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "code" in value:
        out["code"] = value["code"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BatchError:
    out: BatchError = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "code" in data:
        out["code"] = data["code"]
    if "message" in data:
        out["message"] = data["message"]
    return out
