"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Certificates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.certificate

Certificates: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.certificate.Certificate"
]


# --- restJson1 ser/de ---
def serialize_json(value: Certificates) -> list:
    import aws_sdk_bedrock_agentcore.types.certificate

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore.types.certificate.serialize_json(item))
    return out


def deserialize_json(data: list) -> Certificates:
    import aws_sdk_bedrock_agentcore.types.certificate

    out: Certificates = []
    for item in data:
        out.append(aws_sdk_bedrock_agentcore.types.certificate.deserialize_json(item))
    return out
