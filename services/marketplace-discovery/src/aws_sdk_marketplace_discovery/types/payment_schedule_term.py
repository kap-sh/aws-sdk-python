"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#PaymentScheduleTerm``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_discovery.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_discovery.types.currency_code
    import aws_sdk_marketplace_discovery.types.schedule_list
    import aws_sdk_marketplace_discovery.types.term_id
    import aws_sdk_marketplace_discovery.types.term_type


class PaymentScheduleTerm(TypedDict, closed=True):
    id: "aws_sdk_marketplace_discovery.types.term_id.TermId"
    """<p>The unique identifier of the term.</p>"""
    type: "aws_sdk_marketplace_discovery.types.term_type.TermType"
    """<p>The category of the term.</p>"""
    currency_code: "aws_sdk_marketplace_discovery.types.currency_code.CurrencyCode"
    """<p>Defines the currency for the prices in this term.</p>"""
    schedule: "aws_sdk_marketplace_discovery.types.schedule_list.ScheduleList"
    """<p>The payment schedule installments, each with a charge date and amount.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PaymentScheduleTerm) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    import aws_sdk_marketplace_discovery.types.term_type

    out["type"] = aws_sdk_marketplace_discovery.types.term_type.serialize_json(
        value["type"]
    )
    out["currencyCode"] = value["currency_code"]
    import aws_sdk_marketplace_discovery.types.schedule_list

    out["schedule"] = aws_sdk_marketplace_discovery.types.schedule_list.serialize_json(
        value["schedule"]
    )
    return out


def deserialize_json(data: dict) -> PaymentScheduleTerm:
    out: PaymentScheduleTerm = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("PaymentScheduleTerm.id required")
    if "type" in data:
        import aws_sdk_marketplace_discovery.types.term_type

        out["type"] = aws_sdk_marketplace_discovery.types.term_type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("PaymentScheduleTerm.type required")
    if "currencyCode" in data:
        out["currency_code"] = data["currencyCode"]
    else:
        raise DeserializationError("PaymentScheduleTerm.currency_code required")
    if "schedule" in data:
        import aws_sdk_marketplace_discovery.types.schedule_list

        out["schedule"] = (
            aws_sdk_marketplace_discovery.types.schedule_list.deserialize_json(
                data["schedule"]
            )
        )
    else:
        raise DeserializationError("PaymentScheduleTerm.schedule required")
    return out
