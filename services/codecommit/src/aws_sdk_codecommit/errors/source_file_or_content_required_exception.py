"""Generated from Smithy shape ``com.amazonaws.codecommit#SourceFileOrContentRequiredException``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.message


class SourceFileOrContentRequiredException_(TypedDict):
    message: NotRequired["aws_sdk_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceFileOrContentRequiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceFileOrContentRequiredException_:
    out: SourceFileOrContentRequiredException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class SourceFileOrContentRequiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#SourceFileOrContentRequiredException``."""

    code: str | None = "SourceFileOrContentRequiredException"

    def __init__(self, data: SourceFileOrContentRequiredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="SourceFileOrContentRequiredException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "SourceFileOrContentRequiredException":
        return cls(deserialize_aws_json_1_1(data))
