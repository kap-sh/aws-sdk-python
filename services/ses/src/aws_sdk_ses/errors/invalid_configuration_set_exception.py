"""Generated from Smithy shape ``com.amazonaws.ses#InvalidConfigurationSetException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ses.types.error_message


class InvalidConfigurationSetException_(TypedDict):
    message: NotRequired["aws_sdk_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidConfigurationSetException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidConfigurationSetException_:
    out: InvalidConfigurationSetException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidConfigurationSetException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#InvalidConfigurationSetException``."""

    code: str | None = "InvalidConfigurationSetException"

    def __init__(self, data: InvalidConfigurationSetException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidConfigurationSetException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidConfigurationSetException":
        return cls(deserialize_query(el))
