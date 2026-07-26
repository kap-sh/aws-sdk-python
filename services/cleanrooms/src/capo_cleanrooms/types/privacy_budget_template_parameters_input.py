"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyBudgetTemplateParametersInput``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.access_budgets_privacy_template_parameters_input
    import capo_cleanrooms.types.differential_privacy_template_parameters_input


class _PrivacyBudgetTemplateParametersInput_differentialPrivacy(TypedDict, closed=True):
    differentialPrivacy: "capo_cleanrooms.types.differential_privacy_template_parameters_input.DifferentialPrivacyTemplateParametersInput"


class _PrivacyBudgetTemplateParametersInput_accessBudget(TypedDict, closed=True):
    accessBudget: "capo_cleanrooms.types.access_budgets_privacy_template_parameters_input.AccessBudgetsPrivacyTemplateParametersInput"


PrivacyBudgetTemplateParametersInput: TypeAlias = (
    _PrivacyBudgetTemplateParametersInput_differentialPrivacy
    | _PrivacyBudgetTemplateParametersInput_accessBudget
)


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyBudgetTemplateParametersInput) -> dict:
    if "differentialPrivacy" in value:
        import capo_cleanrooms.types.differential_privacy_template_parameters_input

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_template_parameters_input.serialize_json(
                value["differentialPrivacy"]
            )
        }
    elif "accessBudget" in value:
        import capo_cleanrooms.types.access_budgets_privacy_template_parameters_input

        return {
            "accessBudget": capo_cleanrooms.types.access_budgets_privacy_template_parameters_input.serialize_json(
                value["accessBudget"]
            )
        }
    else:
        raise SerializationError(
            "PrivacyBudgetTemplateParametersInput: no variant present"
        )


def deserialize_json(data: dict) -> PrivacyBudgetTemplateParametersInput:
    if "differentialPrivacy" in data:
        import capo_cleanrooms.types.differential_privacy_template_parameters_input

        return {
            "differentialPrivacy": capo_cleanrooms.types.differential_privacy_template_parameters_input.deserialize_json(
                data["differentialPrivacy"]
            )
        }
    elif "accessBudget" in data:
        import capo_cleanrooms.types.access_budgets_privacy_template_parameters_input

        return {
            "accessBudget": capo_cleanrooms.types.access_budgets_privacy_template_parameters_input.deserialize_json(
                data["accessBudget"]
            )
        }
    else:
        raise DeserializationError(
            "PrivacyBudgetTemplateParametersInput: no recognized variant key"
        )
