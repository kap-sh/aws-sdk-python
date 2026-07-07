"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AccessBudgetsPrivacyTemplateParametersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.budget_parameters
    import aws_sdk_cleanrooms.types.budgeted_resource_arn


class AccessBudgetsPrivacyTemplateParametersInput(TypedDict, closed=True):
    budget_parameters: "aws_sdk_cleanrooms.types.budget_parameters.BudgetParameters"
    """<p>An array of budget parameters that define the access budget configuration for the privacy template.</p>"""
    resource_arn: "aws_sdk_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource associated with this privacy budget template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessBudgetsPrivacyTemplateParametersInput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.budget_parameters

    out["budgetParameters"] = aws_sdk_cleanrooms.types.budget_parameters.serialize_json(
        value["budget_parameters"]
    )
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> AccessBudgetsPrivacyTemplateParametersInput:
    out: AccessBudgetsPrivacyTemplateParametersInput = {}  # type: ignore[typeddict-item]
    if "budgetParameters" in data:
        import aws_sdk_cleanrooms.types.budget_parameters

        out["budget_parameters"] = (
            aws_sdk_cleanrooms.types.budget_parameters.deserialize_json(
                data["budgetParameters"]
            )
        )
    else:
        raise DeserializationError(
            "AccessBudgetsPrivacyTemplateParametersInput.budget_parameters required"
        )
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "AccessBudgetsPrivacyTemplateParametersInput.resource_arn required"
        )
    return out
