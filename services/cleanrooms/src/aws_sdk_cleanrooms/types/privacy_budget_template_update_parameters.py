"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PrivacyBudgetTemplateUpdateParameters``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.access_budgets_privacy_template_update_parameters
    import aws_sdk_cleanrooms.types.differential_privacy_template_update_parameters


class _PrivacyBudgetTemplateUpdateParameters_differentialPrivacy(TypedDict):
    differentialPrivacy: "aws_sdk_cleanrooms.types.differential_privacy_template_update_parameters.DifferentialPrivacyTemplateUpdateParameters"


class _PrivacyBudgetTemplateUpdateParameters_accessBudget(TypedDict):
    accessBudget: "aws_sdk_cleanrooms.types.access_budgets_privacy_template_update_parameters.AccessBudgetsPrivacyTemplateUpdateParameters"


PrivacyBudgetTemplateUpdateParameters: TypeAlias = (
    _PrivacyBudgetTemplateUpdateParameters_differentialPrivacy
    | _PrivacyBudgetTemplateUpdateParameters_accessBudget
)


# --- restJson1 ser/de ---
def serialize_json(value: PrivacyBudgetTemplateUpdateParameters) -> dict:
    if "differentialPrivacy" in value:
        import aws_sdk_cleanrooms.types.differential_privacy_template_update_parameters

        return {
            "differentialPrivacy": aws_sdk_cleanrooms.types.differential_privacy_template_update_parameters.serialize_json(
                value["differentialPrivacy"]
            )
        }
    elif "accessBudget" in value:
        import aws_sdk_cleanrooms.types.access_budgets_privacy_template_update_parameters

        return {
            "accessBudget": aws_sdk_cleanrooms.types.access_budgets_privacy_template_update_parameters.serialize_json(
                value["accessBudget"]
            )
        }
    else:
        raise SerializationError(
            "PrivacyBudgetTemplateUpdateParameters: no variant present"
        )


def deserialize_json(data: dict) -> PrivacyBudgetTemplateUpdateParameters:
    if "differentialPrivacy" in data:
        import aws_sdk_cleanrooms.types.differential_privacy_template_update_parameters

        return {
            "differentialPrivacy": aws_sdk_cleanrooms.types.differential_privacy_template_update_parameters.deserialize_json(
                data["differentialPrivacy"]
            )
        }
    elif "accessBudget" in data:
        import aws_sdk_cleanrooms.types.access_budgets_privacy_template_update_parameters

        return {
            "accessBudget": aws_sdk_cleanrooms.types.access_budgets_privacy_template_update_parameters.deserialize_json(
                data["accessBudget"]
            )
        }
    else:
        raise DeserializationError(
            "PrivacyBudgetTemplateUpdateParameters: no recognized variant key"
        )
