"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BatchCreateBillingAdjustmentError``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.billing_adjustment_error_code
    import aws_sdk_marketplace_agreement.types.client_token


class BatchCreateBillingAdjustmentError(TypedDict):
    code: "aws_sdk_marketplace_agreement.types.billing_adjustment_error_code.BillingAdjustmentErrorCode"
    """<p>The error code indicating the reason for failure.</p>"""
    message: "str"
    """<p>A human-readable message describing the error.</p>"""
    client_token: "aws_sdk_marketplace_agreement.types.client_token.ClientToken"
    """<p>The client token of the request entry that failed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateBillingAdjustmentError) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_agreement.types.billing_adjustment_error_code

    out["code"] = (
        aws_sdk_marketplace_agreement.types.billing_adjustment_error_code.serialize_aws_json_1_0(
            value["code"]
        )
    )
    out["message"] = value["message"]
    out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateBillingAdjustmentError:
    out: BatchCreateBillingAdjustmentError = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import aws_sdk_marketplace_agreement.types.billing_adjustment_error_code

        out["code"] = (
            aws_sdk_marketplace_agreement.types.billing_adjustment_error_code.deserialize_aws_json_1_0(
                data["code"]
            )
        )
    else:
        raise DeserializationError("BatchCreateBillingAdjustmentError.code required")
    if "message" in data:
        out["message"] = data["message"]
    else:
        raise DeserializationError("BatchCreateBillingAdjustmentError.message required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    else:
        raise DeserializationError(
            "BatchCreateBillingAdjustmentError.client_token required"
        )
    return out
