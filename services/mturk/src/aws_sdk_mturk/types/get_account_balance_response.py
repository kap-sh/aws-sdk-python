"""Generated from Smithy shape ``com.amazonaws.mturk#GetAccountBalanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mturk.types.currency_amount


class GetAccountBalanceResponse(TypedDict, closed=True):
    available_balance: NotRequired["aws_sdk_mturk.types.currency_amount.CurrencyAmount"]
    on_hold_balance: NotRequired["aws_sdk_mturk.types.currency_amount.CurrencyAmount"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAccountBalanceResponse) -> dict:
    out: dict = {}
    if "available_balance" in value:
        out["AvailableBalance"] = value["available_balance"]
    if "on_hold_balance" in value:
        out["OnHoldBalance"] = value["on_hold_balance"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAccountBalanceResponse:
    out: GetAccountBalanceResponse = {}  # type: ignore[typeddict-item]
    if "AvailableBalance" in data:
        out["available_balance"] = data["AvailableBalance"]
    if "OnHoldBalance" in data:
        out["on_hold_balance"] = data["OnHoldBalance"]
    return out
