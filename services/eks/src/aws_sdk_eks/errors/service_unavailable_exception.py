"""Generated from Smithy shape ``com.amazonaws.eks#ServiceUnavailableException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eks.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_eks.types.string


class ServiceUnavailableException_(TypedDict):
    message: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The request has failed due to a temporary failure of the server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceUnavailableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ServiceUnavailableException_:
    out: ServiceUnavailableException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ServiceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.eks#ServiceUnavailableException``."""

    code: str | None = "ServiceUnavailableException"

    def __init__(self, data: ServiceUnavailableException_):
        super().__init__(
            "server",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceUnavailableException",
        )
        self.data = data

    @classmethod
    def from_json(cls, data: dict) -> "ServiceUnavailableException":
        return cls(deserialize_json(data))
