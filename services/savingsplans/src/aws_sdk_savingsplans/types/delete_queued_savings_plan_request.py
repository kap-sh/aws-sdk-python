"""Generated from Smithy shape ``com.amazonaws.savingsplans#DeleteQueuedSavingsPlanRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_savingsplans.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.savings_plan_id


class DeleteQueuedSavingsPlanRequest(TypedDict):
    savings_plan_id: "aws_sdk_savingsplans.types.savings_plan_id.SavingsPlanId"
    """<p>The ID of the Savings Plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteQueuedSavingsPlanRequest) -> dict:
    out: dict = {}
    out["savingsPlanId"] = value["savings_plan_id"]
    return out


def deserialize_json(data: dict) -> DeleteQueuedSavingsPlanRequest:
    out: DeleteQueuedSavingsPlanRequest = {}  # type: ignore[typeddict-item]
    if "savingsPlanId" in data:
        out["savings_plan_id"] = data["savingsPlanId"]
    else:
        raise DeserializationError(
            "DeleteQueuedSavingsPlanRequest.savings_plan_id required"
        )
    return out
