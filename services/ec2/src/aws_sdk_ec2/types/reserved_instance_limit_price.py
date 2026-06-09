"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstanceLimitPrice``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.currency_code_values
    import aws_sdk_ec2.types.double


class ReservedInstanceLimitPrice(TypedDict):
    amount: NotRequired["aws_sdk_ec2.types.double.Double"]
    """<p>Used for Reserved Instance Marketplace offerings. Specifies the limit price on the total order (instanceCount * price).</p>"""
    currency_code: NotRequired[
        "aws_sdk_ec2.types.currency_code_values.CurrencyCodeValues"
    ]
    """<p>The currency in which the <code>limitPrice</code> amount is specified. At this time, the only supported currency is <code>USD</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstanceLimitPrice, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "amount" in value:
        pairs.append((f"{prefix}.Amount", str(value["amount"])))
    if "currency_code" in value:
        import aws_sdk_ec2.types.currency_code_values

        aws_sdk_ec2.types.currency_code_values.serialize_ec2_query(
            value["currency_code"], pairs, f"{prefix}.CurrencyCode"
        )


def deserialize_ec2_query(el: Element) -> ReservedInstanceLimitPrice:
    out: ReservedInstanceLimitPrice = {}  # type: ignore[typeddict-item]
    child_amount = el.find("Amount")
    if child_amount is not None:
        out["amount"] = float(child_amount.text or "")
    child_currency_code = el.find("CurrencyCode")
    if child_currency_code is not None:
        import aws_sdk_ec2.types.currency_code_values

        out["currency_code"] = (
            aws_sdk_ec2.types.currency_code_values.deserialize_ec2_query(
                child_currency_code
            )
        )
    return out
