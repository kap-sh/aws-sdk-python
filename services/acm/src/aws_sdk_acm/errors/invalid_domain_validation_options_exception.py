"""Generated from Smithy shape ``com.amazonaws.acm#InvalidDomainValidationOptionsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_acm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_acm.types.string


class InvalidDomainValidationOptionsException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_acm.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidDomainValidationOptionsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidDomainValidationOptionsException_:
    out: InvalidDomainValidationOptionsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidDomainValidationOptionsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.acm#InvalidDomainValidationOptionsException``."""

    code: str | None = "InvalidDomainValidationOptionsException"

    def __init__(self, data: InvalidDomainValidationOptionsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidDomainValidationOptionsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidDomainValidationOptionsException":
        return cls(deserialize_aws_json_1_1(data))
