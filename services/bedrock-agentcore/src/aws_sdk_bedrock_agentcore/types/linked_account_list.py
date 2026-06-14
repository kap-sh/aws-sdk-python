"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LinkedAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.linked_account

LinkedAccountList: TypeAlias = list[
    "aws_sdk_bedrock_agentcore.types.linked_account.LinkedAccount"
]


# --- restJson1 ser/de ---
def serialize_json(value: LinkedAccountList) -> list:
    import aws_sdk_bedrock_agentcore.types.linked_account

    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_agentcore.types.linked_account.serialize_json(item))
    return out


def deserialize_json(data: list) -> LinkedAccountList:
    import aws_sdk_bedrock_agentcore.types.linked_account

    out: LinkedAccountList = []
    for item in data:
        out.append(
            aws_sdk_bedrock_agentcore.types.linked_account.deserialize_json(item)
        )
    return out
