"""Generated from Smithy shape ``com.amazonaws.frauddetector#ResourceUnavailableException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_frauddetector.errors import ServiceError

if TYPE_CHECKING:
    import capo_frauddetector.types.string


class ResourceUnavailableException_(TypedDict, closed=True):
    message: NotRequired["capo_frauddetector.types.string.string"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceUnavailableException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceUnavailableException_:
    out: ResourceUnavailableException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ResourceUnavailableException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.frauddetector#ResourceUnavailableException``."""

    code: str | None = "ResourceUnavailableException"

    def __init__(self, data: ResourceUnavailableException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceUnavailableException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceUnavailableException":
        return cls(deserialize_aws_json_1_1(data))
