"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyBuildLog``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_log_entry_list


class AutomatedReasoningPolicyBuildLog(TypedDict):
    entries: "aws_sdk_bedrock.types.automated_reasoning_policy_build_log_entry_list.AutomatedReasoningPolicyBuildLogEntryList"
    """<p>A list of log entries documenting each step in the policy build process, including timestamps, status, and detailed messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyBuildLog) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.automated_reasoning_policy_build_log_entry_list

    out["entries"] = (
        aws_sdk_bedrock.types.automated_reasoning_policy_build_log_entry_list.serialize_json(
            value["entries"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyBuildLog:
    out: AutomatedReasoningPolicyBuildLog = {}  # type: ignore[typeddict-item]
    if "entries" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_build_log_entry_list

        out["entries"] = (
            aws_sdk_bedrock.types.automated_reasoning_policy_build_log_entry_list.deserialize_json(
                data["entries"]
            )
        )
    else:
        raise DeserializationError("AutomatedReasoningPolicyBuildLog.entries required")
    return out
