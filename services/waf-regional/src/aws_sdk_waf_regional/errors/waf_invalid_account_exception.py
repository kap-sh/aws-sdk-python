"""Generated from Smithy shape ``com.amazonaws.wafregional#WAFInvalidAccountException``."""

from typing_extensions import TypedDict

from aws_sdk_waf_regional.errors import ServiceError


class WAFInvalidAccountException_(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WAFInvalidAccountException_) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> WAFInvalidAccountException_:
    out: WAFInvalidAccountException_ = {}  # type: ignore[typeddict-item]
    return out


class WAFInvalidAccountException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.wafregional#WAFInvalidAccountException``."""

    code: str | None = "WAFInvalidAccountException"

    def __init__(self, data: WAFInvalidAccountException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="WAFInvalidAccountException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "WAFInvalidAccountException":
        return cls(deserialize_aws_json_1_1(data))
