"""Generated from Smithy shape ``com.amazonaws.configservice#NoSuchConformancePackException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_config_service.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.error_message


class NoSuchConformancePackException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_config_service.types.error_message.ErrorMessage"]
    """<p>Error executing the command</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NoSuchConformancePackException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NoSuchConformancePackException_:
    out: NoSuchConformancePackException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class NoSuchConformancePackException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.configservice#NoSuchConformancePackException``."""

    code: str | None = "NoSuchConformancePackException"

    def __init__(self, data: NoSuchConformancePackException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="NoSuchConformancePackException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "NoSuchConformancePackException":
        return cls(deserialize_aws_json_1_1(data))
