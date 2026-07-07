"""Generated from Smithy shape ``com.amazonaws.chatbot#CustomActionAttachmentCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.custom_action_attachment_criteria_operator


class CustomActionAttachmentCriteria(TypedDict, closed=True):
    operator: "aws_sdk_chatbot.types.custom_action_attachment_criteria_operator.CustomActionAttachmentCriteriaOperator"
    """<p>The operation to perform on the named variable.</p>"""
    variable_name: "str"
    """<p>The name of the variable to operate on.</p>"""
    value: NotRequired["str"]
    """<p>A value that is compared with the actual value of the variable based on the behavior of the operator.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomActionAttachmentCriteria) -> dict:
    out: dict = {}
    import aws_sdk_chatbot.types.custom_action_attachment_criteria_operator

    out["Operator"] = (
        aws_sdk_chatbot.types.custom_action_attachment_criteria_operator.serialize_json(
            value["operator"]
        )
    )
    out["VariableName"] = value["variable_name"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_json(data: dict) -> CustomActionAttachmentCriteria:
    out: CustomActionAttachmentCriteria = {}  # type: ignore[typeddict-item]
    if "Operator" in data:
        import aws_sdk_chatbot.types.custom_action_attachment_criteria_operator

        out["operator"] = (
            aws_sdk_chatbot.types.custom_action_attachment_criteria_operator.deserialize_json(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("CustomActionAttachmentCriteria.operator required")
    if "VariableName" in data:
        out["variable_name"] = data["VariableName"]
    else:
        raise DeserializationError(
            "CustomActionAttachmentCriteria.variable_name required"
        )
    if "Value" in data:
        out["value"] = data["Value"]
    return out
