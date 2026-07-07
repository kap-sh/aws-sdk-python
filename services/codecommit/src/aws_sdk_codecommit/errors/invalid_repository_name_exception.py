"""Generated from Smithy shape ``com.amazonaws.codecommit#InvalidRepositoryNameException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.message


class InvalidRepositoryNameException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidRepositoryNameException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidRepositoryNameException_:
    out: InvalidRepositoryNameException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidRepositoryNameException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#InvalidRepositoryNameException``."""

    code: str | None = "InvalidRepositoryNameException"

    def __init__(self, data: InvalidRepositoryNameException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidRepositoryNameException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidRepositoryNameException":
        return cls(deserialize_aws_json_1_1(data))
