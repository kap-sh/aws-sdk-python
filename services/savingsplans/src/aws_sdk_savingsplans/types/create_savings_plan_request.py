"""Generated from Smithy shape ``com.amazonaws.savingsplans#CreateSavingsPlanRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_savingsplans.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.amount
    import aws_sdk_savingsplans.types.client_token
    import aws_sdk_savingsplans.types.date_time
    import aws_sdk_savingsplans.types.savings_plan_offering_id
    import aws_sdk_savingsplans.types.tag_map


class CreateSavingsPlanRequest(TypedDict):
    savings_plan_offering_id: (
        "aws_sdk_savingsplans.types.savings_plan_offering_id.SavingsPlanOfferingId"
    )
    """<p>The ID of the offering.</p>"""
    commitment: "aws_sdk_savingsplans.types.amount.Amount"
    """<p>The hourly commitment, in the same currency of the <code>savingsPlanOfferingId</code>. This is a value between 0.001 and 1 million. You cannot specify more than five digits after the decimal point.</p>"""
    upfront_payment_amount: NotRequired["aws_sdk_savingsplans.types.amount.Amount"]
    """<p>The up-front payment amount. This is a whole number between 50 and 99 percent of the total value of the Savings Plan. This parameter is only supported if the payment option is <code>Partial Upfront</code>.</p>"""
    purchase_time: NotRequired["aws_sdk_savingsplans.types.date_time.DateTime"]
    """<p>The purchase time of the Savings Plan in UTC format (YYYY-MM-DDTHH:MM:SSZ).</p>"""
    client_token: NotRequired["aws_sdk_savingsplans.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    tags: NotRequired["aws_sdk_savingsplans.types.tag_map.TagMap"]
    """<p>One or more tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSavingsPlanRequest) -> dict:
    out: dict = {}
    out["savingsPlanOfferingId"] = value["savings_plan_offering_id"]
    out["commitment"] = value["commitment"]
    if "upfront_payment_amount" in value:
        out["upfrontPaymentAmount"] = value["upfront_payment_amount"]
    if "purchase_time" in value:
        import aws_sdk_savingsplans.types.date_time

        out["purchaseTime"] = aws_sdk_savingsplans.types.date_time.serialize_json(
            value["purchase_time"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import aws_sdk_savingsplans.types.tag_map

        out["tags"] = aws_sdk_savingsplans.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateSavingsPlanRequest:
    out: CreateSavingsPlanRequest = {}  # type: ignore[typeddict-item]
    if "savingsPlanOfferingId" in data:
        out["savings_plan_offering_id"] = data["savingsPlanOfferingId"]
    else:
        raise DeserializationError(
            "CreateSavingsPlanRequest.savings_plan_offering_id required"
        )
    if "commitment" in data:
        out["commitment"] = data["commitment"]
    else:
        raise DeserializationError("CreateSavingsPlanRequest.commitment required")
    if "upfrontPaymentAmount" in data:
        out["upfront_payment_amount"] = data["upfrontPaymentAmount"]
    if "purchaseTime" in data:
        import aws_sdk_savingsplans.types.date_time

        out["purchase_time"] = aws_sdk_savingsplans.types.date_time.deserialize_json(
            data["purchaseTime"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "tags" in data:
        import aws_sdk_savingsplans.types.tag_map

        out["tags"] = aws_sdk_savingsplans.types.tag_map.deserialize_json(data["tags"])
    return out
