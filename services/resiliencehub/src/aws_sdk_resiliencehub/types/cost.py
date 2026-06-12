"""Generated from Smithy shape ``com.amazonaws.resiliencehub#Cost``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.cost_frequency
    import aws_sdk_resiliencehub.types.currency_code
    import aws_sdk_resiliencehub.types.double


class Cost(TypedDict):
    amount: "aws_sdk_resiliencehub.types.double.Double"
    """<p>The cost amount.</p>"""
    currency: "aws_sdk_resiliencehub.types.currency_code.CurrencyCode"
    """<p>The cost currency, for example <code>USD</code>.</p>"""
    frequency: "aws_sdk_resiliencehub.types.cost_frequency.CostFrequency"
    """<p>The cost frequency.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Cost) -> dict:
    out: dict = {}
    out["amount"] = value.get("amount", 0)
    out["currency"] = value["currency"]
    import aws_sdk_resiliencehub.types.cost_frequency

    out["frequency"] = aws_sdk_resiliencehub.types.cost_frequency.serialize_json(
        value["frequency"]
    )
    return out


def deserialize_json(data: dict) -> Cost:
    out: Cost = {}  # type: ignore[typeddict-item]
    if "amount" in data:
        out["amount"] = data["amount"]
    else:
        out["amount"] = 0
    if "currency" in data:
        out["currency"] = data["currency"]
    else:
        raise DeserializationError("Cost.currency required")
    if "frequency" in data:
        import aws_sdk_resiliencehub.types.cost_frequency

        out["frequency"] = aws_sdk_resiliencehub.types.cost_frequency.deserialize_json(
            data["frequency"]
        )
    else:
        raise DeserializationError("Cost.frequency required")
    return out
