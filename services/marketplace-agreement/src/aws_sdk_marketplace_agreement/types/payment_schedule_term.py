"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#PaymentScheduleTerm``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.currency_code
    import aws_sdk_marketplace_agreement.types.schedule_list
    import aws_sdk_marketplace_agreement.types.term_id
    import aws_sdk_marketplace_agreement.types.unversioned_term_type


class PaymentScheduleTerm(TypedDict):
    type: NotRequired[
        "aws_sdk_marketplace_agreement.types.unversioned_term_type.UnversionedTermType"
    ]
    """<p>Type of the term.</p>"""
    id: NotRequired["aws_sdk_marketplace_agreement.types.term_id.TermId"]
    """<p>The unique identifier for the term.</p>"""
    currency_code: NotRequired[
        "aws_sdk_marketplace_agreement.types.currency_code.CurrencyCode"
    ]
    """<p>Defines the currency for the prices mentioned in the term. </p>"""
    schedule: NotRequired[
        "aws_sdk_marketplace_agreement.types.schedule_list.ScheduleList"
    ]
    """<p>List of the payment schedule where each element defines one installment of payment. It contains the information necessary for calculating the price.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PaymentScheduleTerm) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "id" in value:
        out["id"] = value["id"]
    if "currency_code" in value:
        out["currencyCode"] = value["currency_code"]
    if "schedule" in value:
        import aws_sdk_marketplace_agreement.types.schedule_list

        out["schedule"] = (
            aws_sdk_marketplace_agreement.types.schedule_list.serialize_aws_json_1_0(
                value["schedule"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PaymentScheduleTerm:
    out: PaymentScheduleTerm = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "id" in data:
        out["id"] = data["id"]
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    if "schedule" in data:
        import aws_sdk_marketplace_agreement.types.schedule_list

        out["schedule"] = (
            aws_sdk_marketplace_agreement.types.schedule_list.deserialize_aws_json_1_0(
                data["schedule"]
            )
        )
    return out
