"""Generated from Smithy shape ``com.amazonaws.savingsplans#CreateSavingsPlanResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.savings_plan_id


class CreateSavingsPlanResponse(TypedDict):
    savings_plan_id: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_id.SavingsPlanId"
    ]
    """<p>The ID of the Savings Plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSavingsPlanResponse) -> dict:
    out: dict = {}
    if "savings_plan_id" in value:
        out["savingsPlanId"] = value["savings_plan_id"]
    return out


def deserialize_json(data: dict) -> CreateSavingsPlanResponse:
    out: CreateSavingsPlanResponse = {}  # type: ignore[typeddict-item]
    if "savingsPlanId" in data:
        out["savings_plan_id"] = data["savingsPlanId"]
    return out
