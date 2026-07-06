"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#VariablePaymentTermConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.iso8601_duration
    import aws_sdk_marketplace_agreement.types.payment_request_approval_strategy


class VariablePaymentTermConfiguration(TypedDict, closed=True):
    payment_request_approval_strategy: "aws_sdk_marketplace_agreement.types.payment_request_approval_strategy.PaymentRequestApprovalStrategy"
    """<p>Defines the strategy for approving payment requests. Values include <code>AUTO_APPROVE_ON_EXPIRATION</code> and <code>WAIT_FOR_APPROVAL</code> </p>"""
    expiration_duration: NotRequired[
        "aws_sdk_marketplace_agreement.types.iso8601_duration.ISO8601Duration"
    ]
    """<p>Defines the duration after which a payment request is automatically approved if no further action is taken. This only applies when the payment request approval strategy is set to <code>AUTO_APPROVE_ON_EXPIRATION</code>. The duration is represented in the ISO_8601 format (e.g., P10D for 10 days).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VariablePaymentTermConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_agreement.types.payment_request_approval_strategy

    out["paymentRequestApprovalStrategy"] = (
        aws_sdk_marketplace_agreement.types.payment_request_approval_strategy.serialize_aws_json_1_0(
            value["payment_request_approval_strategy"]
        )
    )
    if "expiration_duration" in value:
        out["expirationDuration"] = value["expiration_duration"]
    return out


def deserialize_aws_json_1_0(data: dict) -> VariablePaymentTermConfiguration:
    out: VariablePaymentTermConfiguration = {}  # type: ignore[typeddict-item]
    if "paymentRequestApprovalStrategy" in data:
        import aws_sdk_marketplace_agreement.types.payment_request_approval_strategy

        out["payment_request_approval_strategy"] = (
            aws_sdk_marketplace_agreement.types.payment_request_approval_strategy.deserialize_aws_json_1_0(
                data["paymentRequestApprovalStrategy"]
            )
        )
    else:
        raise DeserializationError(
            "VariablePaymentTermConfiguration.payment_request_approval_strategy required"
        )
    if "expirationDuration" in data:
        out["expiration_duration"] = data["expirationDuration"]
    return out
