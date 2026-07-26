"""Generated from Smithy shape ``com.amazonaws.codecommit#MaximumRepositoryNamesExceededException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import capo_codecommit.types.message


class MaximumRepositoryNamesExceededException_(TypedDict, closed=True):
    message: NotRequired["capo_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaximumRepositoryNamesExceededException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MaximumRepositoryNamesExceededException_:
    out: MaximumRepositoryNamesExceededException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class MaximumRepositoryNamesExceededException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#MaximumRepositoryNamesExceededException``."""

    code: str | None = "MaximumRepositoryNamesExceededException"

    def __init__(self, data: MaximumRepositoryNamesExceededException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="MaximumRepositoryNamesExceededException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "MaximumRepositoryNamesExceededException":
        return cls(deserialize_aws_json_1_1(data))
