"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckFindingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_check_finding

AutomatedReasoningCheckFindingList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_check_finding.AutomatedReasoningCheckFinding"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckFindingList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_check_finding

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_check_finding.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningCheckFindingList:
    import aws_sdk_bedrock.types.automated_reasoning_check_finding

    out: AutomatedReasoningCheckFindingList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_check_finding.deserialize_json(
                item
            )
        )
    return out
