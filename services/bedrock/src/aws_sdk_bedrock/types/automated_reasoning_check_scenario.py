"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckScenario``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_logic_statement_list


class AutomatedReasoningCheckScenario(TypedDict, closed=True):
    statements: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_logic_statement_list.AutomatedReasoningLogicStatementList"
    ]
    """<p>List of logical assignments and statements that define this scenario.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckScenario) -> dict:
    out: dict = {}
    if "statements" in value:
        import aws_sdk_bedrock.types.automated_reasoning_logic_statement_list

        out["statements"] = (
            aws_sdk_bedrock.types.automated_reasoning_logic_statement_list.serialize_json(
                value["statements"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningCheckScenario:
    out: AutomatedReasoningCheckScenario = {}  # type: ignore[typeddict-item]
    if "statements" in data:
        import aws_sdk_bedrock.types.automated_reasoning_logic_statement_list

        out["statements"] = (
            aws_sdk_bedrock.types.automated_reasoning_logic_statement_list.deserialize_json(
                data["statements"]
            )
        )
    return out
