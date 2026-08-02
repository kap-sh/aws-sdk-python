"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#InvalidEndPointException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element
from capo_elastic_load_balancing.errors import ServiceError

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.error_description


class InvalidEndPointException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_elastic_load_balancing.types.error_description.ErrorDescription"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidEndPointException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidEndPointException_:
    out: InvalidEndPointException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidEndPointException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.elasticloadbalancing#InvalidEndPointException``."""

    code: str | None = "InvalidEndPointException"

    def __init__(self, data: InvalidEndPointException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidEndPointException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidEndPointException":
        return cls(deserialize_query(el))
