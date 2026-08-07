"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#CapacityReservationPendingException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element
from capo_elastic_load_balancing_v2.errors import ServiceError

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.error_description


class CapacityReservationPendingException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_elastic_load_balancing_v2.types.error_description.ErrorDescription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: CapacityReservationPendingException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_query(el: Element) -> CapacityReservationPendingException_:
    out: CapacityReservationPendingException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CapacityReservationPendingException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticloadbalancingv2#CapacityReservationPendingException``."""

    code: str | None = "CapacityReservationPendingException"

    def __init__(self, data: CapacityReservationPendingException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CapacityReservationPendingException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "CapacityReservationPendingException":
        return cls(deserialize_query(el))
