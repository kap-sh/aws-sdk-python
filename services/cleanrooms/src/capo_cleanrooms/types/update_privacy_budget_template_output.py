"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdatePrivacyBudgetTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.privacy_budget_template


class UpdatePrivacyBudgetTemplateOutput(TypedDict, closed=True):
    privacy_budget_template: (
        "capo_cleanrooms.types.privacy_budget_template.PrivacyBudgetTemplate"
    )
    """<p>Summary of the privacy budget template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePrivacyBudgetTemplateOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.privacy_budget_template

    out["privacyBudgetTemplate"] = (
        capo_cleanrooms.types.privacy_budget_template.serialize_json(
            value["privacy_budget_template"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdatePrivacyBudgetTemplateOutput:
    out: UpdatePrivacyBudgetTemplateOutput = {}  # type: ignore[typeddict-item]
    if "privacyBudgetTemplate" in data:
        import capo_cleanrooms.types.privacy_budget_template

        out["privacy_budget_template"] = (
            capo_cleanrooms.types.privacy_budget_template.deserialize_json(
                data["privacyBudgetTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePrivacyBudgetTemplateOutput.privacy_budget_template required"
        )
    return out
