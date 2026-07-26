"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TooManyActionsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element
from capo_elastic_load_balancing_v2.errors import ServiceError

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.error_description


class TooManyActionsException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_elastic_load_balancing_v2.types.error_description.ErrorDescription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: TooManyActionsException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> TooManyActionsException_:
    out: TooManyActionsException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TooManyActionsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticloadbalancingv2#TooManyActionsException``."""

    code: str | None = "TooManyActionsException"

    def __init__(self, data: TooManyActionsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TooManyActionsException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "TooManyActionsException":
        return cls(deserialize_query(el))
