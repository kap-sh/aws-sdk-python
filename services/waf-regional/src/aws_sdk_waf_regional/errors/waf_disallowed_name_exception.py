"""Generated from Smithy shape ``com.amazonaws.wafregional#WAFDisallowedNameException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_waf_regional.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.error_message


class WAFDisallowedNameException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_waf_regional.types.error_message.errorMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFDisallowedNameException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFDisallowedNameException_:
    out: WAFDisallowedNameException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class WAFDisallowedNameException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafregional#WAFDisallowedNameException``."""

    code: str | None = "WAFDisallowedNameException"

    def __init__(self, data: WAFDisallowedNameException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFDisallowedNameException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFDisallowedNameException":
        return cls(deserialize_aws_json_1_1(data))
