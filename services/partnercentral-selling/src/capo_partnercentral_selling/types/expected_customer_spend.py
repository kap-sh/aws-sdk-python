"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ExpectedCustomerSpend``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.amount
    import capo_partnercentral_selling.types.currency_code
    import capo_partnercentral_selling.types.estimation_url
    import capo_partnercentral_selling.types.payment_frequency


class ExpectedCustomerSpend(TypedDict, closed=True):
    amount: "capo_partnercentral_selling.types.amount.Amount"
    """<p>Represents the estimated monthly revenue that the partner expects to earn from the opportunity. This helps in forecasting financial returns.</p>"""
    currency_code: "capo_partnercentral_selling.types.currency_code.CurrencyCode"
    """<p>Indicates the currency in which the revenue estimate is provided. This helps in understanding the financial impact across different markets. Accepted values are <code>USD</code> (US Dollars) and <code>EUR</code> (Euros). If the AWS Partition is <code>aws-eusc</code> (AWS European Sovereign Cloud), the currency code must be <code>EUR</code>.</p>"""
    frequency: "capo_partnercentral_selling.types.payment_frequency.PaymentFrequency"
    """<p>Indicates how frequently the customer is expected to spend the projected amount. Only the value <code>Monthly</code> is allowed for the <code>Frequency</code> field, representing recurring monthly spend.</p>"""
    target_company: "str"
    """<p>Specifies the name of the partner company that is expected to generate revenue from the opportunity. This field helps track the partner’s involvement in the opportunity. This field only accepts the value <code>AWS</code>. If any other value is provided, the system will automatically set it to <code>AWS</code>.</p>"""
    estimation_url: NotRequired[
        "capo_partnercentral_selling.types.estimation_url.EstimationUrl"
    ]
    """<p>A URL providing additional information or context about the spend estimation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExpectedCustomerSpend) -> dict:
    out: dict = {}
    out["Amount"] = value.get("amount", "")
    import capo_partnercentral_selling.types.currency_code

    out["CurrencyCode"] = (
        capo_partnercentral_selling.types.currency_code.serialize_aws_json_1_0(
            value["currency_code"]
        )
    )
    import capo_partnercentral_selling.types.payment_frequency

    out["Frequency"] = (
        capo_partnercentral_selling.types.payment_frequency.serialize_aws_json_1_0(
            value["frequency"]
        )
    )
    out["TargetCompany"] = value["target_company"]
    if "estimation_url" in value:
        out["EstimationUrl"] = value["estimation_url"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExpectedCustomerSpend:
    out: ExpectedCustomerSpend = {}  # type: ignore[typeddict-item]
    if "Amount" in data:
        out["amount"] = data["Amount"]
    else:
        out["amount"] = ""
    if "CurrencyCode" in data:
        import capo_partnercentral_selling.types.currency_code

        out["currency_code"] = (
            capo_partnercentral_selling.types.currency_code.deserialize_aws_json_1_0(
                data["CurrencyCode"]
            )
        )
    else:
        raise DeserializationError("ExpectedCustomerSpend.currency_code required")
    if "Frequency" in data:
        import capo_partnercentral_selling.types.payment_frequency

        out["frequency"] = (
            capo_partnercentral_selling.types.payment_frequency.deserialize_aws_json_1_0(
                data["Frequency"]
            )
        )
    else:
        raise DeserializationError("ExpectedCustomerSpend.frequency required")
    if "TargetCompany" in data:
        out["target_company"] = data["TargetCompany"]
    else:
        raise DeserializationError("ExpectedCustomerSpend.target_company required")
    if "EstimationUrl" in data:
        out["estimation_url"] = data["EstimationUrl"]
    return out
