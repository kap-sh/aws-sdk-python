"""Generated from Smithy shape ``com.amazonaws.rekognition#ResourceAlreadyExistsException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rekognition.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.string


class ResourceAlreadyExistsException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_rekognition.types.string.String"]
    code: NotRequired["aws_sdk_rekognition.types.string.String"]
    logref: NotRequired["aws_sdk_rekognition.types.string.String"]
    """<p>A universally unique identifier (UUID) for the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "code" in value:
        out["Code"] = value["code"]
    if "logref" in value:
        out["Logref"] = value["logref"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceAlreadyExistsException_:
    out: ResourceAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    if "Code" in data:
        out["code"] = data["Code"]
    if "Logref" in data:
        out["logref"] = data["Logref"]
    return out


class ResourceAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.rekognition#ResourceAlreadyExistsException``."""

    code: str | None = "ResourceAlreadyExistsException"

    def __init__(self, data: ResourceAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ResourceAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data))
