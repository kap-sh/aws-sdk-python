"""Generated from Smithy shape ``com.amazonaws.cloudsearch#BaseException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.error_code
    import aws_sdk_cloudsearch.types.error_message


class BaseException_(TypedDict):
    code: NotRequired["aws_sdk_cloudsearch.types.error_code.ErrorCode"]
    message: NotRequired["aws_sdk_cloudsearch.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: BaseException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "code" in value:
        pairs.append((f"{prefix}.Code", str(value["code"])))
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> BaseException_:
    out: BaseException_ = {}  # type: ignore[typeddict-item]
    child_code = el.find("Code")
    if child_code is not None:
        out["code"] = str(child_code.text or "")
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class BaseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.cloudsearch#BaseException``."""

    code: str | None = "BaseException"

    def __init__(self, data: BaseException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BaseException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "BaseException":
        return cls(deserialize_query(el))
