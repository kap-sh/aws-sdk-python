"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_item_enablement_action
    import aws_sdk_connect.types.evaluation_form_item_enablement_condition


class EvaluationFormItemEnablementConfiguration(TypedDict, closed=True):
    condition: "aws_sdk_connect.types.evaluation_form_item_enablement_condition.EvaluationFormItemEnablementCondition"
    """<p>A condition for item enablement configuration.</p>"""
    action: "aws_sdk_connect.types.evaluation_form_item_enablement_action.EvaluationFormItemEnablementAction"
    """<p>An enablement action that if condition is satisfied. </p>"""
    default_action: NotRequired[
        "aws_sdk_connect.types.evaluation_form_item_enablement_action.EvaluationFormItemEnablementAction"
    ]
    """<p>An enablement action that if condition is not satisfied. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.evaluation_form_item_enablement_condition

    out["Condition"] = (
        aws_sdk_connect.types.evaluation_form_item_enablement_condition.serialize_json(
            value["condition"]
        )
    )
    import aws_sdk_connect.types.evaluation_form_item_enablement_action

    out["Action"] = (
        aws_sdk_connect.types.evaluation_form_item_enablement_action.serialize_json(
            value["action"]
        )
    )
    if "default_action" in value:
        import aws_sdk_connect.types.evaluation_form_item_enablement_action

        out["DefaultAction"] = (
            aws_sdk_connect.types.evaluation_form_item_enablement_action.serialize_json(
                value["default_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormItemEnablementConfiguration:
    out: EvaluationFormItemEnablementConfiguration = {}  # type: ignore[typeddict-item]
    if "Condition" in data:
        import aws_sdk_connect.types.evaluation_form_item_enablement_condition

        out["condition"] = (
            aws_sdk_connect.types.evaluation_form_item_enablement_condition.deserialize_json(
                data["Condition"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationFormItemEnablementConfiguration.condition required"
        )
    if "Action" in data:
        import aws_sdk_connect.types.evaluation_form_item_enablement_action

        out["action"] = (
            aws_sdk_connect.types.evaluation_form_item_enablement_action.deserialize_json(
                data["Action"]
            )
        )
    else:
        raise DeserializationError(
            "EvaluationFormItemEnablementConfiguration.action required"
        )
    if "DefaultAction" in data:
        import aws_sdk_connect.types.evaluation_form_item_enablement_action

        out["default_action"] = (
            aws_sdk_connect.types.evaluation_form_item_enablement_action.deserialize_json(
                data["DefaultAction"]
            )
        )
    return out
