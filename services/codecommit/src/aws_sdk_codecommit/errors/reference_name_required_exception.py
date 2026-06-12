"""Generated from Smithy shape ``com.amazonaws.codecommit#ReferenceNameRequiredException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.message


class ReferenceNameRequiredException_(TypedDict):
    message: NotRequired["aws_sdk_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReferenceNameRequiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReferenceNameRequiredException_:
    out: ReferenceNameRequiredException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class ReferenceNameRequiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#ReferenceNameRequiredException``."""

    code: str | None = "ReferenceNameRequiredException"

    def __init__(self, data: ReferenceNameRequiredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ReferenceNameRequiredException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "ReferenceNameRequiredException":
        return cls(deserialize_aws_json_1_1(data))
