"""Generated from Smithy shape ``com.amazonaws.devicefarm#ServiceAccountException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_device_farm.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.message


class ServiceAccountException_(TypedDict):
    message: NotRequired["aws_sdk_device_farm.types.message.Message"]
    """<p>Any additional information about the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceAccountException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceAccountException_:
    out: ServiceAccountException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ServiceAccountException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.devicefarm#ServiceAccountException``."""

    code: str | None = "ServiceAccountException"

    def __init__(self, data: ServiceAccountException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ServiceAccountException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ServiceAccountException":
        return cls(deserialize_aws_json_1_1(data))
