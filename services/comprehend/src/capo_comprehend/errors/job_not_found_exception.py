"""Generated from Smithy shape ``com.amazonaws.comprehend#JobNotFoundException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_comprehend.errors import ServiceError

if TYPE_CHECKING:
    import capo_comprehend.types.string


class JobNotFoundException_(TypedDict, closed=True):
    message: NotRequired["capo_comprehend.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobNotFoundException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JobNotFoundException_:
    out: JobNotFoundException_ = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out


class JobNotFoundException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.comprehend#JobNotFoundException``."""

    code: str | None = "JobNotFoundException"

    def __init__(self, data: JobNotFoundException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="JobNotFoundException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "JobNotFoundException":
        return cls(deserialize_aws_json_1_1(data))
