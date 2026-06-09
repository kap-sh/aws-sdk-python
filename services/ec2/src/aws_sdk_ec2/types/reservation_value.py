"""Generated from Smithy shape ``com.amazonaws.ec2#ReservationValue``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string


class ReservationValue(TypedDict):
    hourly_price: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The hourly rate of the reservation.</p>"""
    remaining_total_value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The balance of the total value (the sum of remainingUpfrontValue + hourlyPrice * number of hours remaining).</p>"""
    remaining_upfront_value: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The remaining upfront cost of the reservation.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservationValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "hourly_price" in value:
        pairs.append((f"{prefix}.HourlyPrice", str(value["hourly_price"])))
    if "remaining_total_value" in value:
        pairs.append(
            (f"{prefix}.RemainingTotalValue", str(value["remaining_total_value"]))
        )
    if "remaining_upfront_value" in value:
        pairs.append(
            (f"{prefix}.RemainingUpfrontValue", str(value["remaining_upfront_value"]))
        )


def deserialize_ec2_query(el: Element) -> ReservationValue:
    out: ReservationValue = {}  # type: ignore[typeddict-item]
    child_hourly_price = el.find("HourlyPrice")
    if child_hourly_price is not None:
        out["hourly_price"] = str(child_hourly_price.text or "")
    child_remaining_total_value = el.find("RemainingTotalValue")
    if child_remaining_total_value is not None:
        out["remaining_total_value"] = str(child_remaining_total_value.text or "")
    child_remaining_upfront_value = el.find("RemainingUpfrontValue")
    if child_remaining_upfront_value is not None:
        out["remaining_upfront_value"] = str(child_remaining_upfront_value.text or "")
    return out
