"""Generated from Smithy shape ``com.amazonaws.codepipeline#InvalidClientTokenException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codepipeline.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.message


class InvalidClientTokenException_(TypedDict):
    message: NotRequired["aws_sdk_codepipeline.types.message.Message"]
    """<p>The message provided to the user in the event of an exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidClientTokenException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidClientTokenException_:
    out: InvalidClientTokenException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidClientTokenException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#InvalidClientTokenException``."""

    code: str | None = "InvalidClientTokenException"

    def __init__(self, data: InvalidClientTokenException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidClientTokenException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidClientTokenException":
        return cls(deserialize_aws_json_1_1(data))
