"""Generated from Smithy shape ``com.amazonaws.servicequotas#DependencyAccessDeniedException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_service_quotas.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.exception_message


class DependencyAccessDeniedException_(TypedDict):
    message: NotRequired[
        "aws_sdk_service_quotas.types.exception_message.ExceptionMessage"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DependencyAccessDeniedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DependencyAccessDeniedException_:
    out: DependencyAccessDeniedException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class DependencyAccessDeniedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.servicequotas#DependencyAccessDeniedException``."""

    code: str | None = "DependencyAccessDeniedException"

    def __init__(self, data: DependencyAccessDeniedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DependencyAccessDeniedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "DependencyAccessDeniedException":
        return cls(deserialize_aws_json_1_1(data))
