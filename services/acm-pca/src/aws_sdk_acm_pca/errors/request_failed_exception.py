"""Generated from Smithy shape ``com.amazonaws.acmpca#RequestFailedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_acm_pca.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_acm_pca.types.string


class RequestFailedException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_acm_pca.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestFailedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestFailedException_:
    out: RequestFailedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class RequestFailedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.acmpca#RequestFailedException``."""

    code: str | None = "RequestFailedException"

    def __init__(self, data: RequestFailedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RequestFailedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "RequestFailedException":
        return cls(deserialize_aws_json_1_1(data))
