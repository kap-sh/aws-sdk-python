"""Generated from Smithy shape ``com.amazonaws.kafka#UnprocessedScramSecret``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class UnprocessedScramSecret(TypedDict):
    error_code: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>Error code for associate/disassociate failure.</p>"""
    error_message: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>Error message for associate/disassociate failure.</p>"""
    secret_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>AWS Secrets Manager secret ARN.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedScramSecret) -> dict:
    out: dict = {}
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "secret_arn" in value:
        out["secretArn"] = value["secret_arn"]
    return out


def deserialize_json(data: dict) -> UnprocessedScramSecret:
    out: UnprocessedScramSecret = {}  # type: ignore[typeddict-item]
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    return out
