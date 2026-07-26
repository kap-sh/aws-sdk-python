"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#OperationNotPermittedException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_application_discovery_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_application_discovery_service.types.message


class OperationNotPermittedException_(TypedDict, closed=True):
    message: NotRequired["capo_application_discovery_service.types.message.Message"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OperationNotPermittedException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OperationNotPermittedException_:
    out: OperationNotPermittedException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class OperationNotPermittedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.applicationdiscoveryservice#OperationNotPermittedException``."""

    code: str | None = "OperationNotPermittedException"

    def __init__(self, data: OperationNotPermittedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="OperationNotPermittedException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "OperationNotPermittedException":
        return cls(deserialize_aws_json_1_1(data))
