"""Generated from Smithy shape ``com.amazonaws.sts#IDPCommunicationErrorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sts._protocol.xml import Element
from aws_sdk_sts.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_sts.types.idp_communication_error_message


class IDPCommunicationErrorException_(TypedDict, closed=True):
    message: NotRequired[
        "aws_sdk_sts.types.idp_communication_error_message.idpCommunicationErrorMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: IDPCommunicationErrorException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> IDPCommunicationErrorException_:
    out: IDPCommunicationErrorException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class IDPCommunicationErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sts#IDPCommunicationErrorException``."""

    code: str | None = "IDPCommunicationErrorException"

    def __init__(self, data: IDPCommunicationErrorException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IDPCommunicationErrorException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "IDPCommunicationErrorException":
        return cls(deserialize_query(el))
