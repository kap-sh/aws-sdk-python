"""Generated from Smithy shape ``com.amazonaws.ecr#RepositoryAlreadyExistsException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ecr.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecr.types.exception_message


class RepositoryAlreadyExistsException_(TypedDict):
    message: NotRequired["aws_sdk_ecr.types.exception_message.ExceptionMessage"]
    """<p>The error message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryAlreadyExistsException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RepositoryAlreadyExistsException_:
    out: RepositoryAlreadyExistsException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class RepositoryAlreadyExistsException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecr#RepositoryAlreadyExistsException``."""

    code: str | None = "RepositoryAlreadyExistsException"

    def __init__(self, data: RepositoryAlreadyExistsException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="RepositoryAlreadyExistsException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "RepositoryAlreadyExistsException":
        return cls(deserialize_aws_json_1_1(data))
