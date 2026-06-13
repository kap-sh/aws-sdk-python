"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BatchCreateBillingAdjustmentItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.billing_adjustment_request_id
    import aws_sdk_marketplace_agreement.types.client_token


class BatchCreateBillingAdjustmentItem(TypedDict):
    billing_adjustment_request_id: "aws_sdk_marketplace_agreement.types.billing_adjustment_request_id.BillingAdjustmentRequestId"
    """<p>The unique identifier of the created billing adjustment request.</p>"""
    client_token: "aws_sdk_marketplace_agreement.types.client_token.ClientToken"
    """<p>The client token provided in the corresponding request entry.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateBillingAdjustmentItem) -> dict:
    out: dict = {}
    out["billingAdjustmentRequestId"] = value["billing_adjustment_request_id"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateBillingAdjustmentItem:
    out: BatchCreateBillingAdjustmentItem = {}  # type: ignore[typeddict-item]
    if "billingAdjustmentRequestId" in data:
        out["billing_adjustment_request_id"] = data["billingAdjustmentRequestId"]
    else:
        raise DeserializationError(
            "BatchCreateBillingAdjustmentItem.billing_adjustment_request_id required"
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "BatchCreateBillingAdjustmentItem.client_token required"
        )
    return out
