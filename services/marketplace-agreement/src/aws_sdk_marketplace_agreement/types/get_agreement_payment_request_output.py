"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#GetAgreementPaymentRequestOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_marketplace_agreement.types.agreement_id
    import aws_sdk_marketplace_agreement.types.charge_id
    import aws_sdk_marketplace_agreement.types.currency_code
    import aws_sdk_marketplace_agreement.types.payment_request_description
    import aws_sdk_marketplace_agreement.types.payment_request_id
    import aws_sdk_marketplace_agreement.types.payment_request_name
    import aws_sdk_marketplace_agreement.types.payment_request_status
    import aws_sdk_marketplace_agreement.types.payment_request_status_message
    import aws_sdk_marketplace_agreement.types.positive_amount_upto8_decimals


class GetAgreementPaymentRequestOutput(TypedDict):
    payment_request_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.payment_request_id.PaymentRequestId"
    ]
    """<p>The unique identifier of the payment request.</p>"""
    agreement_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_id.AgreementId"
    ]
    """<p>The unique identifier of the agreement associated with this payment request. Use <code>DescribeAgreement</code> to retrieve full agreement details.</p>"""
    status: NotRequired[
        "aws_sdk_marketplace_agreement.types.payment_request_status.PaymentRequestStatus"
    ]
    """<p>The current status of the payment request. Possible values include:</p> <ul> <li> <p> <code>VALIDATING</code> – The payment request is being validated against agreement terms.</p> </li> <li> <p> <code>VALIDATION_FAILED</code> – The payment request failed validation.</p> </li> <li> <p> <code>PENDING_APPROVAL</code> – The payment request is awaiting buyer action.</p> </li> <li> <p> <code>APPROVED</code> – The buyer has approved the payment request.</p> </li> <li> <p> <code>REJECTED</code> – The buyer has rejected the payment request.</p> </li> <li> <p> <code>CANCELLED</code> – The seller has cancelled the payment request.</p> </li> </ul>"""
    status_message: NotRequired[
        "aws_sdk_marketplace_agreement.types.payment_request_status_message.PaymentRequestStatusMessage"
    ]
    """<p>An optional message providing additional context about the payment request status, such as a rejection reason or validation failure details.</p>"""
    name: NotRequired[
        "aws_sdk_marketplace_agreement.types.payment_request_name.PaymentRequestName"
    ]
    """<p>The descriptive name of the payment request.</p>"""
    description: NotRequired[
        "aws_sdk_marketplace_agreement.types.payment_request_description.PaymentRequestDescription"
    ]
    """<p>The detailed description of the payment request, if provided.</p>"""
    charge_id: NotRequired["aws_sdk_marketplace_agreement.types.charge_id.ChargeId"]
    """<p>The unique identifier of the charge created after the payment request is approved. This field is only present for approved payment requests and follows the pattern <code>ch-[a-zA-Z0-9]+</code>.</p>"""
    charge_amount: NotRequired[
        "aws_sdk_marketplace_agreement.types.positive_amount_upto8_decimals.PositiveAmountUpto8Decimals"
    ]
    """<p>The amount charged or to be charged to the buyer.</p>"""
    currency_code: NotRequired[
        "aws_sdk_marketplace_agreement.types.currency_code.CurrencyCode"
    ]
    """<p>The currency code for the charge amount.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the payment request was created.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the payment request was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAgreementPaymentRequestOutput) -> dict:
    out: dict = {}
    if "payment_request_id" in value:
        out["paymentRequestId"] = value["payment_request_id"]
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "status" in value:
        import aws_sdk_marketplace_agreement.types.payment_request_status

        out["status"] = (
            aws_sdk_marketplace_agreement.types.payment_request_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "charge_id" in value:
        out["chargeId"] = value["charge_id"]
    if "charge_amount" in value:
        out["chargeAmount"] = value["charge_amount"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "created_at" in value:
        import aws_sdk_marketplace_agreement.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_marketplace_agreement.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import aws_sdk_marketplace_agreement.types._prelude.timestamp

        out["updatedAt"] = (
            aws_sdk_marketplace_agreement.types._prelude.timestamp.serialize_aws_json_1_0(
                value["updated_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAgreementPaymentRequestOutput:
    out: GetAgreementPaymentRequestOutput = {}  # type: ignore[typeddict-item]
    if "paymentRequestId" in data:
        out["payment_request_id"] = data["paymentRequestId"]
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    if "status" in data:
        import aws_sdk_marketplace_agreement.types.payment_request_status

        out["status"] = (
            aws_sdk_marketplace_agreement.types.payment_request_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "name" in data:
        out["name"] = data["name"]
    if "description" in data:
        out["description"] = data["description"]
    if "chargeId" in data:
        out["charge_id"] = data["chargeId"]
    if "chargeAmount" in data:
        out["charge_amount"] = data["chargeAmount"]
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    if "createdAt" in data:
        import aws_sdk_marketplace_agreement.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_marketplace_agreement.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "updatedAt" in data:
        import aws_sdk_marketplace_agreement.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_marketplace_agreement.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    return out
