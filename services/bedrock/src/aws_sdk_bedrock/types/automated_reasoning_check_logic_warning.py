"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckLogicWarning``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.automated_reasoning_check_logic_warning_type
    import aws_sdk_bedrock.types.automated_reasoning_logic_statement_list


class AutomatedReasoningCheckLogicWarning(TypedDict):
    type: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_check_logic_warning_type.AutomatedReasoningCheckLogicWarningType"
    ]
    """<p>The category of the detected logical issue, such as statements that are always true or always false.</p>"""
    premises: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_logic_statement_list.AutomatedReasoningLogicStatementList"
    ]
    """<p>The logical statements that serve as premises under which the claims are validated.</p>"""
    claims: NotRequired[
        "aws_sdk_bedrock.types.automated_reasoning_logic_statement_list.AutomatedReasoningLogicStatementList"
    ]
    """<p>The logical statements that are validated while assuming the policy and premises.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckLogicWarning) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_bedrock.types.automated_reasoning_check_logic_warning_type

        out["type"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_logic_warning_type.serialize_json(
                value["type"]
            )
        )
    if "premises" in value:
        import aws_sdk_bedrock.types.automated_reasoning_logic_statement_list

        out["premises"] = (
            aws_sdk_bedrock.types.automated_reasoning_logic_statement_list.serialize_json(
                value["premises"]
            )
        )
    if "claims" in value:
        import aws_sdk_bedrock.types.automated_reasoning_logic_statement_list

        out["claims"] = (
            aws_sdk_bedrock.types.automated_reasoning_logic_statement_list.serialize_json(
                value["claims"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningCheckLogicWarning:
    out: AutomatedReasoningCheckLogicWarning = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_bedrock.types.automated_reasoning_check_logic_warning_type

        out["type"] = (
            aws_sdk_bedrock.types.automated_reasoning_check_logic_warning_type.deserialize_json(
                data["type"]
            )
        )
    if "premises" in data:
        import aws_sdk_bedrock.types.automated_reasoning_logic_statement_list

        out["premises"] = (
            aws_sdk_bedrock.types.automated_reasoning_logic_statement_list.deserialize_json(
                data["premises"]
            )
        )
    if "claims" in data:
        import aws_sdk_bedrock.types.automated_reasoning_logic_statement_list

        out["claims"] = (
            aws_sdk_bedrock.types.automated_reasoning_logic_statement_list.deserialize_json(
                data["claims"]
            )
        )
    return out
