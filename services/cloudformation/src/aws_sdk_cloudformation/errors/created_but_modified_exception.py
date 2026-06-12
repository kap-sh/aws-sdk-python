"""Generated from Smithy shape ``com.amazonaws.cloudformation#CreatedButModifiedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.error_message


class CreatedButModifiedException_(TypedDict):
    message: NotRequired["aws_sdk_cloudformation.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CreatedButModifiedException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> CreatedButModifiedException_:
    out: CreatedButModifiedException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CreatedButModifiedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudformation#CreatedButModifiedException``."""

    code: str | None = "CreatedButModifiedException"

    def __init__(self, data: CreatedButModifiedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CreatedButModifiedException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "CreatedButModifiedException":
        return cls(deserialize_query(el))
