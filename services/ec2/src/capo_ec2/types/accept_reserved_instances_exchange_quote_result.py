"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptReservedInstancesExchangeQuoteResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string


class AcceptReservedInstancesExchangeQuoteResult(TypedDict, closed=True):
    exchange_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the successful exchange.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AcceptReservedInstancesExchangeQuoteResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "exchange_id" in value:
        pairs.append((f"{key_prefix}ExchangeId", str(value["exchange_id"])))


def deserialize_ec2_query(el: Element) -> AcceptReservedInstancesExchangeQuoteResult:
    out: AcceptReservedInstancesExchangeQuoteResult = {}  # type: ignore[typeddict-item]
    child_exchange_id = el.find("ExchangeId")
    if child_exchange_id is not None:
        out["exchange_id"] = str(child_exchange_id.text or "")
    return out
