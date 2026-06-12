"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#InvalidRevocationContentException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.error_description


class InvalidRevocationContentException_(TypedDict):
    message: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.error_description.ErrorDescription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidRevocationContentException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidRevocationContentException_:
    out: InvalidRevocationContentException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidRevocationContentException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticloadbalancingv2#InvalidRevocationContentException``."""

    code: str | None = "InvalidRevocationContentException"

    def __init__(self, data: InvalidRevocationContentException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRevocationContentException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidRevocationContentException":
        return cls(deserialize_query(el))
