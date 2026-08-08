"""Generated from Smithy shape ``com.amazonaws.ec2#CancelCapacityReservationFleetError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.cancel_capacity_reservation_fleet_error_code
    import capo_ec2.types.cancel_capacity_reservation_fleet_error_message


class CancelCapacityReservationFleetError(TypedDict, closed=True):
    code: NotRequired[
        "capo_ec2.types.cancel_capacity_reservation_fleet_error_code.CancelCapacityReservationFleetErrorCode"
    ]
    """<p>The error code.</p>"""
    message: NotRequired[
        "capo_ec2.types.cancel_capacity_reservation_fleet_error_message.CancelCapacityReservationFleetErrorMessage"
    ]
    """<p>The error message.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelCapacityReservationFleetError,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "code" in value:
        pairs.append((f"{key_prefix}Code", str(value["code"])))
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_ec2_query(el: Element) -> CancelCapacityReservationFleetError:
    out: CancelCapacityReservationFleetError = {}  # type: ignore[typeddict-item]
    child_code = el.find("code")
    if child_code is not None:
        out["code"] = str(child_code.text or "")
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
