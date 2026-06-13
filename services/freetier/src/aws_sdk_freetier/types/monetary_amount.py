"""Generated from Smithy shape ``com.amazonaws.freetier#MonetaryAmount``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_freetier.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_freetier.types.currency_code
    import aws_sdk_freetier.types.generic_double


class MonetaryAmount(TypedDict):
    amount: "aws_sdk_freetier.types.generic_double.GenericDouble"
    """<p> The aggregated monetary amount of credits earned. </p>"""
    unit: "aws_sdk_freetier.types.currency_code.CurrencyCode"
    """<p> The unit that the monetary amount is given in. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MonetaryAmount) -> dict:
    out: dict = {}
    out["amount"] = value.get("amount", 0)
    import aws_sdk_freetier.types.currency_code

    out["unit"] = aws_sdk_freetier.types.currency_code.serialize_aws_json_1_0(
        value["unit"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> MonetaryAmount:
    out: MonetaryAmount = {}  # type: ignore[typeddict-item]
    if "amount" in data:
        out["amount"] = data["amount"]
    else:
        out["amount"] = 0
    if "unit" in data:
        import aws_sdk_freetier.types.currency_code

        out["unit"] = aws_sdk_freetier.types.currency_code.deserialize_aws_json_1_0(
            data["unit"]
        )
    else:
        raise DeserializationError("MonetaryAmount.unit required")
    return out
