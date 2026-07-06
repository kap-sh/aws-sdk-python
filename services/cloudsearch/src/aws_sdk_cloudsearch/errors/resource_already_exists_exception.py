"""Generated from Smithy shape ``com.amazonaws.cloudsearch#ResourceAlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.error_code
    import aws_sdk_cloudsearch.types.error_message


class ResourceAlreadyExistsException_(TypedDict, closed=True):
    code: NotRequired["aws_sdk_cloudsearch.types.error_code.ErrorCode"]
    message: NotRequired["aws_sdk_cloudsearch.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ResourceAlreadyExistsException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "code" in value:
        pairs.append((f"{prefix}.Code", str(value["code"])))
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> ResourceAlreadyExistsException_:
    out: ResourceAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        out["code"] = str(child_code.text or "")
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class ResourceAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudsearch#ResourceAlreadyExistsException``."""

    code: str | None = "ResourceAlreadyExistsException"

    def __init__(self, data: ResourceAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "ResourceAlreadyExistsException":
        return cls(deserialize_query(el))
