"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdatePrivacyBudgetTemplateOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.privacy_budget_template


class UpdatePrivacyBudgetTemplateOutput(TypedDict):
    privacy_budget_template: (
        "aws_sdk_cleanrooms.types.privacy_budget_template.PrivacyBudgetTemplate"
    )
    """<p>Summary of the privacy budget template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePrivacyBudgetTemplateOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.privacy_budget_template

    out["privacyBudgetTemplate"] = (
        aws_sdk_cleanrooms.types.privacy_budget_template.serialize_json(
            value["privacy_budget_template"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdatePrivacyBudgetTemplateOutput:
    out: UpdatePrivacyBudgetTemplateOutput = {}  # type: ignore[typeddict-item]
    if "privacyBudgetTemplate" in data:
        import aws_sdk_cleanrooms.types.privacy_budget_template

        out["privacy_budget_template"] = (
            aws_sdk_cleanrooms.types.privacy_budget_template.deserialize_json(
                data["privacyBudgetTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePrivacyBudgetTemplateOutput.privacy_budget_template required"
        )
    return out
