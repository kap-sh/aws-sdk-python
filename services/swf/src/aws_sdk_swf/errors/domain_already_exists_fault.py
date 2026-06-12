"""Generated from Smithy shape ``com.amazonaws.swf#DomainAlreadyExistsFault``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_swf.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_swf.types.error_message


class DomainAlreadyExistsFault_(TypedDict):
    message: NotRequired["aws_sdk_swf.types.error_message.ErrorMessage"]
    """<p>A description that may help with diagnosing the cause of the fault.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DomainAlreadyExistsFault_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DomainAlreadyExistsFault_:
    out: DomainAlreadyExistsFault_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class DomainAlreadyExistsFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.swf#DomainAlreadyExistsFault``."""

    code: str | None = "DomainAlreadyExistsFault"

    def __init__(self, data: DomainAlreadyExistsFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DomainAlreadyExistsFault",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_0(cls, data: dict) -> "DomainAlreadyExistsFault":
        return cls(deserialize_aws_json_1_0(data))
