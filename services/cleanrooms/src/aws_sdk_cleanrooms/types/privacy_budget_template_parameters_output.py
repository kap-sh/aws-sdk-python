"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyBudgetTemplateParametersOutput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.access_budgets_privacy_template_parameters_output
    import aws_sdk_cleanrooms.types.differential_privacy_template_parameters_output


class _PrivacyBudgetTemplateParametersOutput_differentialPrivacy(
    TypedDict, closed=True
):
    differentialPrivacy: "aws_sdk_cleanrooms.types.differential_privacy_template_parameters_output.DifferentialPrivacyTemplateParametersOutput"


class _PrivacyBudgetTemplateParametersOutput_accessBudget(TypedDict, closed=True):
    accessBudget: "aws_sdk_cleanrooms.types.access_budgets_privacy_template_parameters_output.AccessBudgetsPrivacyTemplateParametersOutput"


PrivacyBudgetTemplateParametersOutput: TypeAlias = (
    _PrivacyBudgetTemplateParametersOutput_differentialPrivacy
    | _PrivacyBudgetTemplateParametersOutput_accessBudget
)


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyBudgetTemplateParametersOutput) -> dict:
    if "differentialPrivacy" in value:
        import aws_sdk_cleanrooms.types.differential_privacy_template_parameters_output

        return {
            "differentialPrivacy": aws_sdk_cleanrooms.types.differential_privacy_template_parameters_output.serialize_json(
                value["differentialPrivacy"]
            )
        }
    elif "accessBudget" in value:
        import aws_sdk_cleanrooms.types.access_budgets_privacy_template_parameters_output

        return {
            "accessBudget": aws_sdk_cleanrooms.types.access_budgets_privacy_template_parameters_output.serialize_json(
                value["accessBudget"]
            )
        }
    else:
        raise SerializationError(
            "PrivacyBudgetTemplateParametersOutput: no variant present"
        )


def deserialize_json(data: dict) -> PrivacyBudgetTemplateParametersOutput:
    if "differentialPrivacy" in data:
        import aws_sdk_cleanrooms.types.differential_privacy_template_parameters_output

        return {
            "differentialPrivacy": aws_sdk_cleanrooms.types.differential_privacy_template_parameters_output.deserialize_json(
                data["differentialPrivacy"]
            )
        }
    elif "accessBudget" in data:
        import aws_sdk_cleanrooms.types.access_budgets_privacy_template_parameters_output

        return {
            "accessBudget": aws_sdk_cleanrooms.types.access_budgets_privacy_template_parameters_output.deserialize_json(
                data["accessBudget"]
            )
        }
    else:
        raise DeserializationError(
            "PrivacyBudgetTemplateParametersOutput: no recognized variant key"
        )
