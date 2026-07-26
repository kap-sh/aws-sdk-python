"""Generated from Smithy shape ``com.amazonaws.acmpca#RequestInProgressException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_acm_pca.errors import ServiceError

if TYPE_CHECKING:
    import capo_acm_pca.types.string


class RequestInProgressException_(TypedDict, closed=True):
    message: NotRequired["capo_acm_pca.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestInProgressException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestInProgressException_:
    out: RequestInProgressException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class RequestInProgressException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.acmpca#RequestInProgressException``."""

    code: str | None = "RequestInProgressException"

    def __init__(self, data: RequestInProgressException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestInProgressException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "RequestInProgressException":
        return cls(deserialize_aws_json_1_1(data))
