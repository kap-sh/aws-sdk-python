"""Generated from Smithy shape ``com.amazonaws.savingsplans#ReturnSavingsPlanResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.savings_plan_id


class ReturnSavingsPlanResponse(TypedDict, closed=True):
    savings_plan_id: NotRequired[
        "aws_sdk_savingsplans.types.savings_plan_id.SavingsPlanId"
    ]
    """<p>The ID of the Savings Plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReturnSavingsPlanResponse) -> dict:
    out: dict = {}
    if "savings_plan_id" in value:
        out["savingsPlanId"] = value["savings_plan_id"]
    return out


def deserialize_json(data: dict) -> ReturnSavingsPlanResponse:
    out: ReturnSavingsPlanResponse = {}  # type: ignore[typeddict-item]
    if "savingsPlanId" in data:
        out["savings_plan_id"] = data["savingsPlanId"]
    return out
