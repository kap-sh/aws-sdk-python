"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyAnnotatedContent``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_policy_annotated_line


class _AutomatedReasoningPolicyAnnotatedContent_line(TypedDict):
    line: "aws_sdk_bedrock.types.automated_reasoning_policy_annotated_line.AutomatedReasoningPolicyAnnotatedLine"


AutomatedReasoningPolicyAnnotatedContent: TypeAlias = (
    _AutomatedReasoningPolicyAnnotatedContent_line
)


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyAnnotatedContent) -> dict:
    if "line" in value:
        import aws_sdk_bedrock.types.automated_reasoning_policy_annotated_line

        return {
            "line": aws_sdk_bedrock.types.automated_reasoning_policy_annotated_line.serialize_json(
                value["line"]
            )
        }
    else:
        raise SerializationError(
            "AutomatedReasoningPolicyAnnotatedContent: no variant present"
        )


def deserialize_json(data: dict) -> AutomatedReasoningPolicyAnnotatedContent:
    if "line" in data:
        import aws_sdk_bedrock.types.automated_reasoning_policy_annotated_line

        return {
            "line": aws_sdk_bedrock.types.automated_reasoning_policy_annotated_line.deserialize_json(
                data["line"]
            )
        }
    else:
        raise DeserializationError(
            "AutomatedReasoningPolicyAnnotatedContent: no recognized variant key"
        )
