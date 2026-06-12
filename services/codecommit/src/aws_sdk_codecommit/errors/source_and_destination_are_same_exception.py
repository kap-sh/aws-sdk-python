"""Generated from Smithy shape ``com.amazonaws.codecommit#SourceAndDestinationAreSameException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.message


class SourceAndDestinationAreSameException_(TypedDict):
    message: NotRequired["aws_sdk_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceAndDestinationAreSameException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceAndDestinationAreSameException_:
    out: SourceAndDestinationAreSameException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class SourceAndDestinationAreSameException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#SourceAndDestinationAreSameException``."""

    code: str | None = "SourceAndDestinationAreSameException"

    def __init__(self, data: SourceAndDestinationAreSameException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SourceAndDestinationAreSameException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "SourceAndDestinationAreSameException":
        return cls(deserialize_aws_json_1_1(data))
