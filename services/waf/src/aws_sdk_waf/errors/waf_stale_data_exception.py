"""Generated from Smithy shape ``com.amazonaws.waf#WAFStaleDataException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_waf.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_waf.types.error_message


class WAFStaleDataException_(TypedDict):
    message: NotRequired["aws_sdk_waf.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFStaleDataException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFStaleDataException_:
    out: WAFStaleDataException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class WAFStaleDataException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.waf#WAFStaleDataException``."""

    code: str | None = "WAFStaleDataException"

    def __init__(self, data: WAFStaleDataException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFStaleDataException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFStaleDataException":
        return cls(deserialize_aws_json_1_1(data))
