"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ServerSideEncryptionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.kms_key_arn


class ServerSideEncryptionConfiguration(TypedDict, closed=True):
    kms_key_arn: NotRequired["aws_sdk_bedrock_agent.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerSideEncryptionConfiguration) -> dict:
    out: dict = {}
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> ServerSideEncryptionConfiguration:
    out: ServerSideEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
