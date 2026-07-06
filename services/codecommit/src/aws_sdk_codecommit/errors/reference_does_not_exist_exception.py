"""Generated from Smithy shape ``com.amazonaws.codecommit#ReferenceDoesNotExistException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.message


class ReferenceDoesNotExistException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReferenceDoesNotExistException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReferenceDoesNotExistException_:
    out: ReferenceDoesNotExistException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ReferenceDoesNotExistException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#ReferenceDoesNotExistException``."""

    code: str | None = "ReferenceDoesNotExistException"

    def __init__(self, data: ReferenceDoesNotExistException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ReferenceDoesNotExistException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ReferenceDoesNotExistException":
        return cls(deserialize_aws_json_1_1(data))
