"""Generated from Smithy shape ``com.amazonaws.sts#IDPRejectedClaimException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element
from capo_sts.errors import ServiceError

if TYPE_CHECKING:
    import capo_sts.types.idp_rejected_claim_message


class IDPRejectedClaimException_(TypedDict, closed=True):
    message: NotRequired[
        "capo_sts.types.idp_rejected_claim_message.idpRejectedClaimMessage"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: IDPRejectedClaimException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> IDPRejectedClaimException_:
    out: IDPRejectedClaimException_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class IDPRejectedClaimException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.sts#IDPRejectedClaimException``."""

    code: str | None = "IDPRejectedClaimException"

    def __init__(self, data: IDPRejectedClaimException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="IDPRejectedClaimException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "IDPRejectedClaimException":
        return cls(deserialize_query(el))
