"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#FirehoseConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.arn_type


class FirehoseConfigurationType(TypedDict, closed=True):
    stream_arn: NotRequired["capo_cognito_identity_provider.types.arn_type.ArnType"]
    """<p>The ARN of an Amazon Data Firehose stream that's the destination for threat protection log export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirehoseConfigurationType) -> dict:
    out: dict = {}
    if "stream_arn" in value:
        out["StreamArn"] = value["stream_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FirehoseConfigurationType:
    out: FirehoseConfigurationType = {}  # type: ignore[typeddict-item]
    if "StreamArn" in data:
        out["stream_arn"] = data["StreamArn"]
    return out
