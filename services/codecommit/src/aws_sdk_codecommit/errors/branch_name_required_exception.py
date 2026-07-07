"""Generated from Smithy shape ``com.amazonaws.codecommit#BranchNameRequiredException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecommit.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.message


class BranchNameRequiredException_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_codecommit.types.message.Message"]
    """<p>Any message associated with the exception.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BranchNameRequiredException_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BranchNameRequiredException_:
    out: BranchNameRequiredException_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class BranchNameRequiredException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.codecommit#BranchNameRequiredException``."""

    code: str | None = "BranchNameRequiredException"

    def __init__(self, data: BranchNameRequiredException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BranchNameRequiredException",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "BranchNameRequiredException":
        return cls(deserialize_aws_json_1_1(data))
