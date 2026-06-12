"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildLogEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_log_entry

AutomatedReasoningPolicyBuildLogEntryList: TypeAlias = list[
    "aws_sdk_bedrock.types.automated_reasoning_policy_build_log_entry.AutomatedReasoningPolicyBuildLogEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildLogEntryList) -> list:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_log_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_build_log_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningPolicyBuildLogEntryList:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_log_entry

    out: AutomatedReasoningPolicyBuildLogEntryList = []
    for item in data:
        out.append(
            aws_sdk_bedrock.types.automated_reasoning_policy_build_log_entry.deserialize_json(
                item
            )
        )
    return out
