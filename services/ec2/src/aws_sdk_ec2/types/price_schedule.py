"""Generated from Smithy shape ``com.amazonaws.ec2#PriceSchedule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.currency_code_values
    import aws_sdk_ec2.types.double
    import aws_sdk_ec2.types.long


class PriceSchedule(TypedDict, closed=True):
    active: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The current price schedule, as determined by the term remaining for the Reserved Instance in the listing.</p> <p>A specific price schedule is always in effect, but only one price schedule can be active at any time. Take, for example, a Reserved Instance listing that has five months remaining in its term. When you specify price schedules for five months and two months, this means that schedule 1, covering the first three months of the remaining term, will be active during months 5, 4, and 3. Then schedule 2, covering the last two months of the term, will be active for months 2 and 1.</p>"""
    currency_code: NotRequired[
        "aws_sdk_ec2.types.currency_code_values.CurrencyCodeValues"
    ]
    """<p>The currency for transacting the Reserved Instance resale. At this time, the only supported currency is <code>USD</code>.</p>"""
    price: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>The fixed price for the term.</p>"""
    term: NotRequired["aws_sdk_ec2.types.long.Long"]
    """<p>The number of months remaining in the reservation. For example, 2 is the second to the last month before the capacity reservation expires.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PriceSchedule, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "active" in value:
        pairs.append((f"{prefix}.Active", "true" if value["active"] else "false"))
    if "currency_code" in value:
        import aws_sdk_ec2.types.currency_code_values

        aws_sdk_ec2.types.currency_code_values.serialize_ec2_query(
            value["currency_code"], pairs, f"{prefix}.CurrencyCode"
        )
    if "price" in value:
        pairs.append((f"{prefix}.Price", str(value["price"])))
    if "term" in value:
        pairs.append((f"{prefix}.Term", str(value["term"])))


def deserialize_ec2_query(el: Element) -> PriceSchedule:
    out: PriceSchedule = {}  # type: ignore[typeddict-item]
    child_active = el.find("Active")
    if child_active is not None:
        out["active"] = (child_active.text or "").lower() == "true"
    child_currency_code = el.find("CurrencyCode")
    if child_currency_code is not None:
        import aws_sdk_ec2.types.currency_code_values

        out["currency_code"] = (
            aws_sdk_ec2.types.currency_code_values.deserialize_ec2_query(
                child_currency_code
            )
        )
    child_price = el.find("Price")
    if child_price is not None:
        out["price"] = float(child_price.text or "")
    child_term = el.find("Term")
    if child_term is not None:
        out["term"] = int(child_term.text or "")
    return out
