"""Generated from Smithy shape ``com.amazonaws.invoicing#CurrencyExchangeDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.basic_string


class CurrencyExchangeDetails(TypedDict):
    source_currency_code: NotRequired[
        "aws_sdk_invoicing.types.basic_string.BasicString"
    ]
    """<p>The exchange source currency. </p>"""
    target_currency_code: NotRequired[
        "aws_sdk_invoicing.types.basic_string.BasicString"
    ]
    """<p>The exchange target currency. </p>"""
    rate: NotRequired["aws_sdk_invoicing.types.basic_string.BasicString"]
    """<p>The currency exchange rate. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CurrencyExchangeDetails) -> dict:
    out: dict = {}
    if "source_currency_code" in value:
        out["SourceCurrencyCode"] = value["source_currency_code"]
    if "target_currency_code" in value:
        out["TargetCurrencyCode"] = value["target_currency_code"]
    if "rate" in value:
        out["Rate"] = value["rate"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CurrencyExchangeDetails:
    out: CurrencyExchangeDetails = {}  # type: ignore[typeddict-item]
    if "SourceCurrencyCode" in data:
        out["source_currency_code"] = data["SourceCurrencyCode"]
    if "TargetCurrencyCode" in data:
        out["target_currency_code"] = data["TargetCurrencyCode"]
    if "Rate" in data:
        out["rate"] = data["Rate"]
    return out
