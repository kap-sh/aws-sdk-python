"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TooManyTrustStoresException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.error_description


class TooManyTrustStoresException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.error_description.ErrorDescription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: TooManyTrustStoresException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> TooManyTrustStoresException_:
    out: TooManyTrustStoresException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TooManyTrustStoresException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticloadbalancingv2#TooManyTrustStoresException``."""

    code: str | None = "TooManyTrustStoresException"

    def __init__(self, data: TooManyTrustStoresException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyTrustStoresException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "TooManyTrustStoresException":
        return cls(deserialize_query(el))
