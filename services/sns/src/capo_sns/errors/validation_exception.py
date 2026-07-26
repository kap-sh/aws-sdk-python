"""Generated from Smithy shape ``com.amazonaws.sns#ValidationException``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import DeserializationError, ServiceError

if TYPE_CHECKING:
    import capo_sns.types.string


class ValidationException_(TypedDict, closed=True):
    message: "capo_sns.types.string.String"


# --- awsQuery ser/de ---
def serialize_query(
    value: ValidationException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> ValidationException_:
    out: ValidationException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    else:
        raise DeserializationError("ValidationException_.message required")
    return out


class ValidationException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sns#ValidationException``."""

    code: str | None = "ValidationException"

    def __init__(self, data: ValidationException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ValidationException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "ValidationException":
        return cls(deserialize_query(el))
