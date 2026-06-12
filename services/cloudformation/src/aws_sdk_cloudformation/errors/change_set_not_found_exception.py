"""Generated from Smithy shape ``com.amazonaws.cloudformation#ChangeSetNotFoundException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudformation.types.error_message


class ChangeSetNotFoundException_(TypedDict):
    message: NotRequired["aws_sdk_cloudformation.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ChangeSetNotFoundException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> ChangeSetNotFoundException_:
    out: ChangeSetNotFoundException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ChangeSetNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudformation#ChangeSetNotFoundException``."""

    code: str | None = "ChangeSetNotFoundException"

    def __init__(self, data: ChangeSetNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ChangeSetNotFoundException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "ChangeSetNotFoundException":
        return cls(deserialize_query(el))
