"""Generated from Smithy shape ``com.amazonaws.codecommit#FileContentRequiredException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import capo_codecommit.types.message


class FileContentRequiredException_(TypedDict, closed=True):
    message: NotRequired["capo_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileContentRequiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FileContentRequiredException_:
    out: FileContentRequiredException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class FileContentRequiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#FileContentRequiredException``."""

    code: str | None = "FileContentRequiredException"

    def __init__(self, data: FileContentRequiredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="FileContentRequiredException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "FileContentRequiredException":
        return cls(deserialize_aws_json_1_1(data))
