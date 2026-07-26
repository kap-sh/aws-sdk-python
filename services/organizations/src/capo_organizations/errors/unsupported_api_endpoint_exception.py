"""Generated from Smithy shape ``com.amazonaws.organizations#UnsupportedAPIEndpointException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_organizations.errors import ServiceError

if TYPE_CHECKING:
    import capo_organizations.types.exception_message


class UnsupportedAPIEndpointException_(TypedDict, closed=True):
    message: NotRequired["capo_organizations.types.exception_message.ExceptionMessage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnsupportedAPIEndpointException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnsupportedAPIEndpointException_:
    out: UnsupportedAPIEndpointException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class UnsupportedAPIEndpointException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.organizations#UnsupportedAPIEndpointException``."""

    code: str | None = "UnsupportedAPIEndpointException"

    def __init__(self, data: UnsupportedAPIEndpointException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="UnsupportedAPIEndpointException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "UnsupportedAPIEndpointException":
        return cls(deserialize_aws_json_1_1(data))
