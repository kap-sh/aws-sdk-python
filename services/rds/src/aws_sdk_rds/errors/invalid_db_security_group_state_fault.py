"""Generated from Smithy shape ``com.amazonaws.rds#InvalidDBSecurityGroupStateFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rds.types.exception_message


class InvalidDBSecurityGroupStateFault_(TypedDict):
    message: NotRequired["aws_sdk_rds.types.exception_message.ExceptionMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: InvalidDBSecurityGroupStateFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> InvalidDBSecurityGroupStateFault_:
    out: InvalidDBSecurityGroupStateFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class InvalidDBSecurityGroupStateFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rds#InvalidDBSecurityGroupStateFault``."""

    code: str | None = "InvalidDBSecurityGroupStateFault"

    def __init__(self, data: InvalidDBSecurityGroupStateFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidDBSecurityGroupStateFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "InvalidDBSecurityGroupStateFault":
        return cls(deserialize_query(el))
