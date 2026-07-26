"""Generated from Smithy shape ``com.amazonaws.iam#OpenIdIdpCommunicationErrorException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iam._protocol.xml import Element
from capo_iam.errors import ServiceError

if TYPE_CHECKING:
    import capo_iam.types.open_id_idp_communication_error_exception_message


class OpenIdIdpCommunicationErrorException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_iam.types.open_id_idp_communication_error_exception_message.openIdIdpCommunicationErrorExceptionMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: OpenIdIdpCommunicationErrorException_,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> OpenIdIdpCommunicationErrorException_:
    out: OpenIdIdpCommunicationErrorException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class OpenIdIdpCommunicationErrorException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.iam#OpenIdIdpCommunicationErrorException``."""

    code: str | None = "OpenIdIdpCommunicationErrorException"

    def __init__(self, data: OpenIdIdpCommunicationErrorException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OpenIdIdpCommunicationErrorException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "OpenIdIdpCommunicationErrorException":
        return cls(deserialize_query(el))
