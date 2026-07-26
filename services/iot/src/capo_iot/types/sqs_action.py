"""Generated from Smithy shape ``com.amazonaws.iot#SqsAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot.types.aws_arn
    import capo_iot.types.queue_url
    import capo_iot.types.use_base64


class SqsAction(TypedDict, closed=True):
    role_arn: "capo_iot.types.aws_arn.AwsArn"
    """<p>The ARN of the IAM role that grants access.</p>"""
    queue_url: "capo_iot.types.queue_url.QueueUrl"
    """<p>The URL of the Amazon SQS queue.</p>"""
    use_base64: NotRequired["capo_iot.types.use_base64.UseBase64"]
    """<p>Specifies whether to use Base64 encoding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SqsAction) -> dict:
    out: dict = {}
    out["roleArn"] = value["role_arn"]
    out["queueUrl"] = value["queue_url"]
    if "use_base64" in value:
        out["useBase64"] = value["use_base64"]
    return out


def deserialize_json(data: dict) -> SqsAction:
    out: SqsAction = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("SqsAction.role_arn required")
    if "queueUrl" in data:
        out["queue_url"] = data["queueUrl"]
    else:
        raise DeserializationError("SqsAction.queue_url required")
    if "useBase64" in data:
        out["use_base64"] = data["useBase64"]
    return out
