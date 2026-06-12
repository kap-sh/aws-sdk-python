"""Generated from Smithy shape ``com.amazonaws.savingsplans#ReturnSavingsPlanRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_savingsplans.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.client_token
    import aws_sdk_savingsplans.types.savings_plan_id


class ReturnSavingsPlanRequest(TypedDict):
    savings_plan_id: "aws_sdk_savingsplans.types.savings_plan_id.SavingsPlanId"
    """<p>The ID of the Savings Plan.</p>"""
    client_token: NotRequired["aws_sdk_savingsplans.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReturnSavingsPlanRequest) -> dict:
    out: dict = {}
    out["savingsPlanId"] = value["savings_plan_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> ReturnSavingsPlanRequest:
    out: ReturnSavingsPlanRequest = {}  # type: ignore[typeddict-item]
    if "savingsPlanId" in data:
        out["savings_plan_id"] = data["savingsPlanId"]
    else:
        raise DeserializationError("ReturnSavingsPlanRequest.savings_plan_id required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
