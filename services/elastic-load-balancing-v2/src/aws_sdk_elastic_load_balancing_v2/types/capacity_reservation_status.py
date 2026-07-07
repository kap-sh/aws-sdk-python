"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#CapacityReservationStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.capacity_reservation_state_enum
    import aws_sdk_elastic_load_balancing_v2.types.state_reason


class CapacityReservationStatus(TypedDict, closed=True):
    code: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.capacity_reservation_state_enum.CapacityReservationStateEnum"
    ]
    """<p>The status code.</p>"""
    reason: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.state_reason.StateReason"
    ]
    """<p>The reason code for the status.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CapacityReservationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "code" in value:
        import aws_sdk_elastic_load_balancing_v2.types.capacity_reservation_state_enum

        aws_sdk_elastic_load_balancing_v2.types.capacity_reservation_state_enum.serialize_query(
            value["code"], pairs, f"{prefix}.Code"
        )
    if "reason" in value:
        pairs.append((f"{prefix}.Reason", str(value["reason"])))


def deserialize_query(el: Element) -> CapacityReservationStatus:
    out: CapacityReservationStatus = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        import aws_sdk_elastic_load_balancing_v2.types.capacity_reservation_state_enum

        out["code"] = (
            aws_sdk_elastic_load_balancing_v2.types.capacity_reservation_state_enum.deserialize_query(
                child_code
            )
        )
    child_reason = el.find("Reason")
    if child_reason is not None:
        out["reason"] = str(child_reason.text or "")
    return out
