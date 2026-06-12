"""Generated from Smithy shape ``com.amazonaws.codecommit#InvalidReactionValueException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.message


class InvalidReactionValueException_(TypedDict):
    message: NotRequired["aws_sdk_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidReactionValueException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidReactionValueException_:
    out: InvalidReactionValueException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class InvalidReactionValueException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#InvalidReactionValueException``."""

    code: str | None = "InvalidReactionValueException"

    def __init__(self, data: InvalidReactionValueException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidReactionValueException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "InvalidReactionValueException":
        return cls(deserialize_aws_json_1_1(data))
