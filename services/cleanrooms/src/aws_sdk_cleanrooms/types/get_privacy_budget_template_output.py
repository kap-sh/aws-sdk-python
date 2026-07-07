"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetPrivacyBudgetTemplateOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.privacy_budget_template


class GetPrivacyBudgetTemplateOutput(TypedDict, closed=True):
    privacy_budget_template: (
        "aws_sdk_cleanrooms.types.privacy_budget_template.PrivacyBudgetTemplate"
    )
    """<p>Returns the details of the privacy budget template that you requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPrivacyBudgetTemplateOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.privacy_budget_template

    out["privacyBudgetTemplate"] = (
        aws_sdk_cleanrooms.types.privacy_budget_template.serialize_json(
            value["privacy_budget_template"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetPrivacyBudgetTemplateOutput:
    out: GetPrivacyBudgetTemplateOutput = {}  # type: ignore[typeddict-item]
    if "privacyBudgetTemplate" in data:
        import aws_sdk_cleanrooms.types.privacy_budget_template

        out["privacy_budget_template"] = (
            aws_sdk_cleanrooms.types.privacy_budget_template.deserialize_json(
                data["privacyBudgetTemplate"]
            )
        )
    else:
        raise DeserializationError(
            "GetPrivacyBudgetTemplateOutput.privacy_budget_template required"
        )
    return out
