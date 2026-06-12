"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#MonetaryValue``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.currency_code


class MonetaryValue(TypedDict):
    amount: "str"
    """<p>Specifies the payment amount.</p>"""
    currency_code: "aws_sdk_partnercentral_selling.types.currency_code.CurrencyCode"
    """<p>Specifies the payment currency. Accepted values are <code>USD</code> (US Dollars) and <code>EUR</code> (Euros). If the AWS Partition is <code>aws-eusc</code> (AWS European Sovereign Cloud), the currency code must be <code>EUR</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MonetaryValue) -> dict:
    out: dict = {}
    out["Amount"] = value["amount"]
    import aws_sdk_partnercentral_selling.types.currency_code

    out["CurrencyCode"] = (
        aws_sdk_partnercentral_selling.types.currency_code.serialize_aws_json_1_0(
            value["currency_code"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> MonetaryValue:
    out: MonetaryValue = {}  # type: ignore[typeddict-item]
    if "Amount" in data:
        out["amount"] = data["Amount"]
    else:
        raise DeserializationError("MonetaryValue.amount required")
    if "CurrencyCode" in data:
        import aws_sdk_partnercentral_selling.types.currency_code

        out["currency_code"] = (
            aws_sdk_partnercentral_selling.types.currency_code.deserialize_aws_json_1_0(
                data["CurrencyCode"]
            )
        )
    else:
        raise DeserializationError("MonetaryValue.currency_code required")
    return out
