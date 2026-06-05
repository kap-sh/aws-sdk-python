"""Generated from Smithy shape ``com.amazonaws.ec2#PriceScheduleSpecification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.currency_code_values
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.long


class PriceScheduleSpecification(TypedDict):
    term: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The number of months remaining in the reservation. For example, 2 is the second to the last month before the capacity reservation expires.</p>"""
    price: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The fixed price for the term.</p>"""
    currency_code: NotRequired[
        "aws_sdk_ec2.types.currency_code_values.CurrencyCodeValues"
    ]
    """<p>The currency for transacting the Reserved Instance resale. At this time, the only supported currency is <code>USD</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PriceScheduleSpecification, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "term" in value:
        pairs.append((f"{prefix}.Term", str(value["term"])))
    if "price" in value:
        pairs.append((f"{prefix}.Price", str(value["price"])))
    if "currency_code" in value:
        import aws_sdk_ec2.types.currency_code_values

        aws_sdk_ec2.types.currency_code_values.serialize_ec2_query(
            value["currency_code"], pairs, f"{prefix}.CurrencyCode"
        )


def deserialize_ec2_query(el: Element) -> PriceScheduleSpecification:
    out: PriceScheduleSpecification = {}  # type: ignore[typeddict-item]
    child_term = el.find("Term")
    if child_term is not None:
        out["term"] = int(child_term.text or "")
    child_price = el.find("Price")
    if child_price is not None:
        out["price"] = float(child_price.text or "")
    child_currency_code = el.find("CurrencyCode")
    if child_currency_code is not None:
        import aws_sdk_ec2.types.currency_code_values

        out["currency_code"] = (
            aws_sdk_ec2.types.currency_code_values.deserialize_ec2_query(
                child_currency_code
            )
        )
    return out
