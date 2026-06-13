"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AccessBudgetsPrivacyTemplateParametersOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.budget_parameters
    import aws_sdk_cleanrooms.types.budgeted_resource_arn


class AccessBudgetsPrivacyTemplateParametersOutput(TypedDict):
    budget_parameters: "aws_sdk_cleanrooms.types.budget_parameters.BudgetParameters"
    """<p>An array of budget parameters returned from the access budget configuration.</p>"""
    resource_arn: "aws_sdk_cleanrooms.types.budgeted_resource_arn.BudgetedResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource associated with this privacy budget template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AccessBudgetsPrivacyTemplateParametersOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.budget_parameters

    out["budgetParameters"] = aws_sdk_cleanrooms.types.budget_parameters.serialize_json(
        value["budget_parameters"]
    )
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> AccessBudgetsPrivacyTemplateParametersOutput:
    out: AccessBudgetsPrivacyTemplateParametersOutput = {}  # type: ignore[typeddict-item]
    if "budgetParameters" in data:
        import aws_sdk_cleanrooms.types.budget_parameters

        out["budget_parameters"] = (
            aws_sdk_cleanrooms.types.budget_parameters.deserialize_json(
                data["budgetParameters"]
            )
        )
    else:
        raise DeserializationError(
            "AccessBudgetsPrivacyTemplateParametersOutput.budget_parameters required"
        )
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "AccessBudgetsPrivacyTemplateParametersOutput.resource_arn required"
        )
    return out
