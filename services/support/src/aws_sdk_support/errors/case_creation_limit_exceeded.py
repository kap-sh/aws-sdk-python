"""Generated from Smithy shape ``com.amazonaws.support#CaseCreationLimitExceeded``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_support.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_support.types.error_message


class CaseCreationLimitExceeded_(TypedDict):
    message: NotRequired["aws_sdk_support.types.error_message.ErrorMessage"]
    """<p>An error message that indicates that you have exceeded the number of cases you can have open.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CaseCreationLimitExceeded_) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CaseCreationLimitExceeded_:
    out: CaseCreationLimitExceeded_ = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out


class CaseCreationLimitExceeded(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.support#CaseCreationLimitExceeded``."""

    code: str | None = "CaseCreationLimitExceeded"

    def __init__(self, data: CaseCreationLimitExceeded_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CaseCreationLimitExceeded",
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(cls, data: dict) -> "CaseCreationLimitExceeded":
        return cls(deserialize_aws_json_1_1(data))
