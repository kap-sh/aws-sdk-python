"""Generated from Smithy shape ``com.amazonaws.iam#CallerIsNotManagementAccountException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_iam.types.exception_message


class CallerIsNotManagementAccountException_(TypedDict):
    message: NotRequired["aws_sdk_iam.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CallerIsNotManagementAccountException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.Message", str(value["message"])))


def deserialize_query(el: Element) -> CallerIsNotManagementAccountException_:
    out: CallerIsNotManagementAccountException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("Message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CallerIsNotManagementAccountException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#CallerIsNotManagementAccountException``."""

    code: str | None = "CallerIsNotManagementAccountException"

    def __init__(self, data: CallerIsNotManagementAccountException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CallerIsNotManagementAccountException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "CallerIsNotManagementAccountException":
        return cls(deserialize_query(el))
