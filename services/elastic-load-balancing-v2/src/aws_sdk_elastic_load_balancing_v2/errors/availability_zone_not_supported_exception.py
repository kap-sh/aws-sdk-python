"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#AvailabilityZoneNotSupportedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.error_description


class AvailabilityZoneNotSupportedException_(TypedDict):
    message: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.error_description.ErrorDescription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailabilityZoneNotSupportedException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> AvailabilityZoneNotSupportedException_:
    out: AvailabilityZoneNotSupportedException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class AvailabilityZoneNotSupportedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticloadbalancingv2#AvailabilityZoneNotSupportedException``."""

    code: str | None = "AvailabilityZoneNotSupportedException"

    def __init__(self, data: AvailabilityZoneNotSupportedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="AvailabilityZoneNotSupportedException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "AvailabilityZoneNotSupportedException":
        return cls(deserialize_query(el))
