"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#KmsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.key_type
    import aws_sdk_bedrock_agentcore_control.types.kms_key_arn


class KmsConfiguration(TypedDict):
    key_type: "aws_sdk_bedrock_agentcore_control.types.key_type.KeyType"
    """<p>The type of KMS key (CustomerManagedKey or ServiceManagedKey).</p>"""
    kms_key_arn: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KmsConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.key_type

    out["keyType"] = aws_sdk_bedrock_agentcore_control.types.key_type.serialize_json(
        value["key_type"]
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> KmsConfiguration:
    out: KmsConfiguration = {}  # type: ignore[typeddict-item]
    if "keyType" in data:
        import aws_sdk_bedrock_agentcore_control.types.key_type

        out["key_type"] = (
            aws_sdk_bedrock_agentcore_control.types.key_type.deserialize_json(
                data["keyType"]
            )
        )
    else:
        raise DeserializationError("KmsConfiguration.key_type required")
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
