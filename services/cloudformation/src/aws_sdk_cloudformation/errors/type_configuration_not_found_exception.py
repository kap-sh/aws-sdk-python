"""Generated from Smithy shape ``com.amazonaws.cloudformation#TypeConfigurationNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.error_message


class TypeConfigurationNotFoundException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_cloudformation.types.error_message.ErrorMessage"]
    """<p>A message with details about the error that occurred.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TypeConfigurationNotFoundException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> TypeConfigurationNotFoundException_:
    out: TypeConfigurationNotFoundException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class TypeConfigurationNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudformation#TypeConfigurationNotFoundException``."""

    code: str | None = "TypeConfigurationNotFoundException"

    def __init__(self, data: TypeConfigurationNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="TypeConfigurationNotFoundException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "TypeConfigurationNotFoundException":
        return cls(deserialize_query(el))
