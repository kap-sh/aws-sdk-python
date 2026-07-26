"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#PaymentRequestSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.payment_request_summary

PaymentRequestSummaryList: TypeAlias = list[
    "capo_marketplace_agreement.types.payment_request_summary.PaymentRequestSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PaymentRequestSummaryList) -> list:
    import capo_marketplace_agreement.types.payment_request_summary

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.payment_request_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> PaymentRequestSummaryList:
    import capo_marketplace_agreement.types.payment_request_summary

    out: PaymentRequestSummaryList = []
    for item in data:
        out.append(
            capo_marketplace_agreement.types.payment_request_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
