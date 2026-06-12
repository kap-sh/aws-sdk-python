"""Generated from Smithy shape ``com.amazonaws.connect#NumericQuestionPropertyValueAutomation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.numeric_question_property_automation_label


class NumericQuestionPropertyValueAutomation(TypedDict):
    label: "aws_sdk_connect.types.numeric_question_property_automation_label.NumericQuestionPropertyAutomationLabel"
    """<p>The property label of the automation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumericQuestionPropertyValueAutomation) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.numeric_question_property_automation_label

    out["Label"] = (
        aws_sdk_connect.types.numeric_question_property_automation_label.serialize_json(
            value["label"]
        )
    )
    return out


def deserialize_json(data: dict) -> NumericQuestionPropertyValueAutomation:
    out: NumericQuestionPropertyValueAutomation = {}  # type: ignore[typeddict-item]
    if "Label" in data:
        import aws_sdk_connect.types.numeric_question_property_automation_label

        out["label"] = (
            aws_sdk_connect.types.numeric_question_property_automation_label.deserialize_json(
                data["Label"]
            )
        )
    else:
        raise DeserializationError(
            "NumericQuestionPropertyValueAutomation.label required"
        )
    return out
