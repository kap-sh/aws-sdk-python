"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#SSLPolicyNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.error_description


class SSLPolicyNotFoundException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_elastic_load_balancing_v2.types.error_description.ErrorDescription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: SSLPolicyNotFoundException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> SSLPolicyNotFoundException_:
    out: SSLPolicyNotFoundException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class SSLPolicyNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticloadbalancingv2#SSLPolicyNotFoundException``."""

    code: str | None = "SSLPolicyNotFoundException"

    def __init__(self, data: SSLPolicyNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SSLPolicyNotFoundException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "SSLPolicyNotFoundException":
        return cls(deserialize_query(el))
