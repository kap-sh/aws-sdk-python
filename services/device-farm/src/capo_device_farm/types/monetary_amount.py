"""Generated from Smithy shape ``com.amazonaws.devicefarm#MonetaryAmount``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.currency_code
    import capo_device_farm.types.double


class MonetaryAmount(TypedDict, closed=True):
    amount: NotRequired["capo_device_farm.types.double.Double"]
    """<p>The numerical amount of an offering or transaction.</p>"""
    currency_code: NotRequired["capo_device_farm.types.currency_code.CurrencyCode"]
    """<p>The currency code of a monetary amount. For example, <code>USD</code> means U.S. dollars.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonetaryAmount) -> dict:
    out: dict = {}
    if "amount" in value:
        out["amount"] = value["amount"]
    if "currency_code" in value:
        import capo_device_farm.types.currency_code

        out["currencyCode"] = (
            capo_device_farm.types.currency_code.serialize_aws_json_1_1(
                value["currency_code"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonetaryAmount:
    out: MonetaryAmount = {}  # type: ignore[typeddict-item]
    if "amount" in data:
        out["amount"] = data["amount"]
    if "currencyCode" in data:
        import capo_device_farm.types.currency_code

        out["currency_code"] = (
            capo_device_farm.types.currency_code.deserialize_aws_json_1_1(
                data["currencyCode"]
            )
        )
    return out
