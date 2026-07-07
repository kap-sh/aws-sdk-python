"""Generated from Smithy shape ``com.amazonaws.codepipeline#InvalidJobStateException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codepipeline.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.message


class InvalidJobStateException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codepipeline.types.message.Message"]
    """<p>The message provided to the user in the event of an exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidJobStateException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidJobStateException_:
    out: InvalidJobStateException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidJobStateException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codepipeline#InvalidJobStateException``."""

    code: str | None = "InvalidJobStateException"

    def __init__(self, data: InvalidJobStateException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidJobStateException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidJobStateException":
        return cls(deserialize_aws_json_1_1(data))
