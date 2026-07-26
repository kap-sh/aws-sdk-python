"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreatePrivacyBudgetTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.privacy_budget_template


class CreatePrivacyBudgetTemplateOutput(TypedDict, closed=True):
    privacy_budget_template: (
        "capo_cleanrooms.types.privacy_budget_template.PrivacyBudgetTemplate"
    )
    """<p>A summary of the elements in the privacy budget template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePrivacyBudgetTemplateOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.privacy_budget_template

    out["privacyBudgetTemplate"] = (
        capo_cleanrooms.types.privacy_budget_template.serialize_json(
            value["privacy_budget_template"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreatePrivacyBudgetTemplateOutput:
    out: CreatePrivacyBudgetTemplateOutput = {}  # type: ignore[typeddict-item]
    if "privacyBudgetTemplate" in data:
        import capo_cleanrooms.types.privacy_budget_template

        out["privacy_budget_template"] = (
            capo_cleanrooms.types.privacy_budget_template.deserialize_json(
                data["privacyBudgetTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePrivacyBudgetTemplateOutput.privacy_budget_template required"
        )
    return out
